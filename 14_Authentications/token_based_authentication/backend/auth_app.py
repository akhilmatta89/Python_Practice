from datetime import datetime, timedelta, timezone
from typing import Optional, Dict
import os

from dotenv import load_dotenv
load_dotenv()

import jwt
from fastapi import FastAPI, Depends, HTTPException, status, Response, Cookie
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel, Field

# =============================
# CONFIG
# =============================
SECRET_KEY = os.getenv("JWT_SECRET", "CHANGE_ME_TO_A_LONG_RANDOM_VALUE")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Cookie config (dev-friendly defaults)
COOKIE_NAME = "refresh_token"
COOKIE_SECURE = os.getenv("COOKIE_SECURE", "false").lower() == "true"
COOKIE_SAMESITE = "lax"
COOKIE_PATH = "/"

FRONTEND_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
    # optional tuning (reasonable defaults below)
    argon2__memory_cost=102400,    # 100 MB
    argon2__time_cost=2,
    argon2__parallelism=8,
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

app = FastAPI(title="Token-based Auth Demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================
# Models
# =============================
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=128)
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    full_name: Optional[str] = None

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int

class TokenOnly(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int

class TokenPayload(BaseModel):
    sub: str
    typ: str
    exp: int

# =============================
# Fake DB
# =============================
class UserInDB(BaseModel):
    username: str
    password_hash: str
    full_name: Optional[str] = None

DB: Dict[str, UserInDB] = {}

# =============================
# Helpers
# =============================
def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_token(*, subject: str, token_type: str, expires_delta: timedelta) -> str:
    now = datetime.now(tz=timezone.utc)
    payload = {
        "sub": subject,
        "typ": token_type,
        "iat": int(now.timestamp()),
        "exp": int((now + expires_delta).timestamp()),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_access_token(username: str) -> str:
    return create_token(
        subject=username,
        token_type="access",
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )

def create_refresh_token(username: str) -> str:
    return create_token(
        subject=username,
        token_type="refresh",
        expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
    )

def decode_token_raw(token: str) -> TokenPayload:
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return TokenPayload(**data)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    payload = decode_token_raw(token)
    if payload.typ != "access":
        raise HTTPException(status_code=401, detail="Access token required")
    user = DB.get(payload.sub)
    if not user:
        raise HTTPException(status_code=401, detail="User no longer exists")
    return user

# =============================
# Routes
# =============================
@app.post("/auth/signup", response_model=UserOut, status_code=201)
def signup(body: UserCreate):
    if body.username in DB:
        raise HTTPException(status_code=409, detail="Username already exists")
    DB[body.username] = UserInDB(
        username=body.username,
        password_hash=hash_password(body.password),
        full_name=body.full_name,
    )
    return UserOut(username=body.username, full_name=body.full_name)

@app.post("/auth/login", response_model=Token)
def login(response: Response, form: OAuth2PasswordRequestForm = Depends()):
    user = DB.get(form.username)
    if not user or not verify_password(form.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access = create_access_token(user.username)
    refresh = create_refresh_token(user.username)

    response.set_cookie(
        key=COOKIE_NAME,
        value=refresh,
        httponly=True,
        secure=COOKIE_SECURE,
        samesite=COOKIE_SAMESITE,
        path=COOKIE_PATH,
        max_age=REFRESH_TOKEN_EXPIRE_DAYS * 24 * 3600,
    )

    return Token(
        access_token=access,
        refresh_token="(stored in httpOnly cookie)",
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )

@app.post("/auth/refresh", response_model=TokenOnly)
def refresh_token(response: Response, refresh_token: Optional[str] = Cookie(default=None, alias=COOKIE_NAME)):
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Missing refresh token")
    payload = decode_token_raw(refresh_token)
    if payload.typ != "refresh":
        raise HTTPException(status_code=401, detail="Refresh token required")

    # TODO (prod): check rotation/denylist
    new_access = create_access_token(payload.sub)
    new_refresh = create_refresh_token(payload.sub)

    response.set_cookie(
        key=COOKIE_NAME,
        value=new_refresh,
        httponly=True,
        secure=COOKIE_SECURE,
        samesite=COOKIE_SAMESITE,
        path=COOKIE_PATH,
        max_age=REFRESH_TOKEN_EXPIRE_DAYS * 24 * 3600,
    )

    return TokenOnly(access_token=new_access, expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60)

@app.post("/auth/logout")
def logout(response: Response):
    response.delete_cookie(key=COOKIE_NAME, path=COOKIE_PATH)
    return {"ok": True}

@app.get("/me", response_model=UserOut)
def me(current: UserInDB = Depends(get_current_user)):
    return UserOut(username=current.username, full_name=current.full_name)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

# Run: uvicorn auth_app:app --reload
