from fastapi import Depends, HTTPException, status, Request
import jwt

from .config import JWT_SECRET, JWT_ALGORITHM
from .blacklist import is_blacklisted

def get_token_from_auth_header(request: Request) -> str:
    auth = request.headers.get("Authorization")
    if not auth or not auth.lower().startswith("bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    return auth.split(" ", 1)[1].strip()

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user_claims(token: str = Depends(get_token_from_auth_header)) -> dict:
    claims = decode_token(token)
    if claims.get("scope") != "access":
        raise HTTPException(status_code=401, detail="Invalid token scope")
    # Optional: if you added a jti for access token revocation, check it here
    return claims

def require_roles(required: list[str]):
    def _guard(claims: dict = Depends(get_current_user_claims)):
        roles = claims.get("roles", [])
        if not any(r in roles for r in required):
            raise HTTPException(status_code=403, detail="Insufficient role")
        return claims
    return _guard
