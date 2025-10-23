from passlib.hash import argon2 as argon2_hasher
import uvicorn
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field
from passlib.hash import bcrypt
import jwt
import datetime
from typing import Dict, Optional

# =============================
# CONFIG
# =============================
JWT_SECRET = "CHANGE_ME_TO_A_LONG_RANDOM_SECRET"  # use env var in production
JWT_ALG = "HS256"
ACCESS_TOKEN_MINUTES = 30

# =============================
# "DATABASE" (in-memory demo)
# =============================
class User(BaseModel):
    username: str
    password_hash: str
    full_name: Optional[str] = None

# username -> User
USERS: Dict[str, User] = {}

# =============================
# SCHEMAS
# =============================
class RegisterIn(BaseModel):
    username: str = Field(min_length=3, max_length=64, pattern=r"^[a-zA-Z0-9_.-]+$")
    password: str = Field(min_length=8, max_length=72)  # bcrypt’s max
    full_name: Optional[str] = None

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int

class ProfileOut(BaseModel):
    username: str
    full_name: Optional[str] = None

# =============================
# APP
# =============================
app = FastAPI(title="Password-based Auth API (FastAPI demo)")

bearer = HTTPBearer(auto_error=False)

def create_access_token(sub: str) -> str:
    now = datetime.datetime.utcnow()
    payload = {
        "iss": "password-auth-demo",
        "sub": sub,
        "iat": now,
        "exp": now + datetime.timedelta(minutes=ACCESS_TOKEN_MINUTES),
        "scope": "access"
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)

def verify_token(token: str) -> str:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
        if payload.get("scope") != "access":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token scope")
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def current_username(creds: HTTPAuthorizationCredentials = Depends(bearer)) -> str:
    if not creds:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")
    return verify_token(creds.credentials)

# =============================
# ROUTES
# =============================

@app.post("/register", status_code=201)
def register(body: RegisterIn):
    # 1) Validate uniqueness
    if body.username in USERS:
        raise HTTPException(status_code=409, detail="Username already exists")

    # 2) Hash password using Argon2 (includes salt internally)
    pw_hash = argon2_hasher.hash(body.password)

    # 3) Store user
    USERS[body.username] = User(
        username=body.username,
        password_hash=pw_hash,
        full_name=body.full_name
    )
    return {"message": "Registered successfully"}

@app.post("/login", response_model=TokenOut)
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = USERS.get(form.username)
    # verify password against stored hash
    if not user or not argon2_hasher.verify(form.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token(sub=user.username)
    return TokenOut(access_token=token, expires_in=ACCESS_TOKEN_MINUTES * 60)


@app.get("/me", response_model=ProfileOut)
def me(username: str = Depends(current_username)):
    user = USERS.get(username)
    return ProfileOut(username=user.username, full_name=user.full_name)

# Simple health check
@app.get("/healthz")
def healthz():
    return {"ok": True}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000, reload=False)
