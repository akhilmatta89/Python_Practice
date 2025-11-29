from flask import Flask, request, jsonify
import logging
import requests

app = Flask(__name__)

# ------------------ Logging Setup ------------------
logger = logging.getLogger("ip_logger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


# ------------------ Helper: Get client IP ------------------
def get_client_ip():
    forwarded_for = request.headers.get("X-Forwarded-For")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    return request.remote_addr or "unknown"


# ------------------ Helpers: EC2 metadata (IMDSv2-aware) ------------------
def get_metadata(path: str) -> str:
    """
    Fetch metadata from AWS IMDSv2, falling back to IMDSv1 if needed.
    Works only from inside an EC2 instance.
    """
    base_url = "http://169.254.169.254"
    timeout = 2
    token = None

    # Try IMDSv2 token
    try:
        token_resp = requests.put(
            f"{base_url}/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=timeout,
        )
        if token_resp.status_code == 200:
            token = token_resp.text
        else:
            logger.warning(
                f"IMDSv2 token request failed with status {token_resp.status_code}"
            )
    except Exception as e:
        logger.warning(f"Could not fetch IMDSv2 token: {e}")

    headers = {}
    if token:
        headers["X-aws-ec2-metadata-token"] = token

    try:
        resp = requests.get(
            f"{base_url}/latest/meta-data/{path}",
            headers=headers,
            timeout=timeout,
        )
        if resp.status_code == 200 and resp.text.strip():
            return resp.text.strip()
        else:
            logger.warning(
                f"Metadata request for '{path}' returned status {resp.status_code}"
            )
            return "Not Available"
    except Exception as e:
        logger.error(f"Failed to fetch metadata '{path}': {e}")
        return "Not Available"


def get_ec2_private_ip():
    return get_metadata("local-ipv4")


def get_ec2_public_ip():
    return get_metadata("public-ipv4")


def get_server_ips():
    private_ip = get_ec2_private_ip()
    public_ip = get_ec2_public_ip()
    return private_ip, public_ip


# ------------------ Request logging ------------------
@app.before_request
def log_request():
    client_ip = get_client_ip()
    server_private_ip, server_public_ip = get_server_ips()

    logger.info(
        f"Request: method={request.method}, path={request.path}, "
        f"client_ip={client_ip}, private_ip={server_private_ip}, public_ip={server_public_ip}"
    )


# ------------------ Routes ------------------

@app.route("/", methods=["GET"])
def home():
    client_ip = get_client_ip()
    server_private_ip, server_public_ip = get_server_ips()

    msg = (
        f"Hello! Your IP is {client_ip}, "
        f"server private IP is {server_private_ip}, "
        f"server public IP is {server_public_ip}"
    )
    logger.info(f"[HOME] {msg}")
    return jsonify({
        "message": msg,
        "client_ip": client_ip,
        "server_private_ip": server_private_ip,
        "server_public_ip": server_public_ip,
    })


@app.route("/ping", methods=["GET"])
def ping():
    client_ip = get_client_ip()
    server_private_ip, server_public_ip = get_server_ips()
    logger.info(f"[PING] Ping from {client_ip}")
    return jsonify({
        "status": "ok",
        "from_ip": client_ip,
        "server_private_ip": server_private_ip,
        "server_public_ip": server_public_ip,
    })


@app.route("/log-demo", methods=["POST"])
def log_demo():
    client_ip = get_client_ip()
    server_private_ip, server_public_ip = get_server_ips()
    logger.info(f"[LOG-DEMO] Demo log from {client_ip}")
    return jsonify({
        "message": "Demo log printed",
        "from_ip": client_ip,
        "server_private_ip": server_private_ip,
        "server_public_ip": server_public_ip,
    })


@app.route("/echo", methods=["GET"])
def echo():
    msg = request.args.get("msg", "no message sent")
    client_ip = get_client_ip()
    server_private_ip, server_public_ip = get_server_ips()
    logger.info(f"[ECHO] From {client_ip}: {msg}")
    return jsonify({
        "echo": msg,
        "from_ip": client_ip,
        "server_private_ip": server_private_ip,
        "server_public_ip": server_public_ip,
    })


@app.route("/internet-check", methods=["GET"])
def internet_check():
    client_ip = get_client_ip()
    server_private_ip, server_public_ip = get_server_ips()
    logger.info(f"[INTERNET CHECK] Started for {client_ip}")

    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        data = response.json()

        logger.info(f"[INTERNET CHECK] Success → {data}")

        return jsonify({
            "status": "internet_ok",
            "public_ip_lookup": data,
            "server_private_ip": server_private_ip,
            "server_public_ip": server_public_ip,
            "message": "Server successfully made an external internet call"
        })

    except Exception as e:
        logger.error(f"[INTERNET CHECK] Failed → {str(e)}")
        return jsonify({
            "status": "internet_failed",
            "error": str(e),
            "server_private_ip": server_private_ip,
            "server_public_ip": server_public_ip,
            "message": "Server could NOT reach the internet"
        }), 500


# ------------------ Run Server ------------------

if __name__ == "__main__":
    priv, pub = get_server_ips()
    logger.info("Starting Flask server")
    logger.info(f"  Private IP (dynamic): {priv}")
    logger.info(f"  Public  IP (dynamic): {pub}")
    logger.info("Server running on port 5005")
    app.run(host="0.0.0.0", port=5005, debug=True)
