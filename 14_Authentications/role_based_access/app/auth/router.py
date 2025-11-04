from fastapi import APIRouter, HTTPException, status, Response, Request
from typing import Tuple
import jwt

from .models import RegisterIn, LoginIn, TokenOut, User
from .config import (
    REFRESH_COOKIE_NAME, REFRESH_COOKIE_PATH, REFRESH_COOKIE_SAMESITE,
    REFRESH_COOKIE_SECURE, REFRESH_COOKIE_HTTPONLY
)
from .tokens import create_access_token, create_refresh_token
from .deps import decode_token
from .blacklist import add_to_blacklist, is_blacklisted
from .storage.memory import create_user, get_user_by_email
from app.core.security import verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

# --------- REGISTER ----------
@router.post("/register")
def register_user(body: RegisterIn):
    try:
        user = create_user(email=body.email, password=body.password, roles=body.roles)
    except ValueError:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"message": "User registered successfully", "user": {"email": user.email, "roles": user.roles}}

# --------- LOGIN ----------
@router.post("/login", response_model=TokenOut)
def login(body: LoginIn, response: Response):
    user = get_user_by_email(body.email)
    if not user or not verify_password(body.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access = create_access_token(user_id=user.id, roles=user.roles)
    refresh, tid = create_refresh_token(user_id=user.id)

    # Set refresh token cookie
    response.set_cookie(
        key=REFRESH_COOKIE_NAME,
        value=refresh,
        httponly=REFRESH_COOKIE_HTTPONLY,
        secure=REFRESH_COOKIE_SECURE,
        samesite=REFRESH_COOKIE_SAMESITE,  # "strict"
        path=REFRESH_COOKIE_PATH,
    )
    return TokenOut(access_token=access)

# --------- REFRESH (ROTATION) ----------
@router.post("/refresh", response_model=TokenOut)
def refresh(request: Request, response: Response):
    refresh_cookie = request.cookies.get(REFRESH_COOKIE_NAME)
    if not refresh_cookie:
        raise HTTPException(status_code=401, detail="Missing refresh token")

    claims = decode_token(refresh_cookie)
    if claims.get("scope") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid token scope")

    tid = str(claims.get("tid", ""))
    if not tid:
        raise HTTPException(status_code=401, detail="Malformed refresh token")

    if is_blacklisted(tid):
        raise HTTPException(status_code=401, detail="Refresh token already used")

    # blacklist old refresh tid until exp
    exp_epoch = int(claims.get("exp"))
    add_to_blacklist(tid, exp_epoch)

    user_id = claims["sub"]

    # ✅ Fetch roles by user_id so admin stays admin after refresh
    from .storage.memory import get_user_by_id
    user = get_user_by_id(user_id)
    roles = user.roles if user else ["user"]

    access_new = create_access_token(user_id=user_id, roles=roles)
    refresh_new, tid_new = create_refresh_token(user_id=user_id)

    response.set_cookie(
        key=REFRESH_COOKIE_NAME,
        value=refresh_new,
        httponly=REFRESH_COOKIE_HTTPONLY,
        secure=REFRESH_COOKIE_SECURE,
        samesite=REFRESH_COOKIE_SAMESITE,
        path=REFRESH_COOKIE_PATH,
    )
    return TokenOut(access_token=access_new)


# --------- LOGOUT ----------
@router.post("/logout")
def logout(request: Request, response: Response):
    refresh_cookie = request.cookies.get(REFRESH_COOKIE_NAME)
    if refresh_cookie:
        try:
            claims = decode_token(refresh_cookie)
            if claims.get("scope") == "refresh":
                tid = str(claims.get("tid", ""))
                exp_epoch = int(claims.get("exp"))
                if tid:
                    add_to_blacklist(tid, exp_epoch)
        except Exception:
            pass

    response.delete_cookie(REFRESH_COOKIE_NAME, path=REFRESH_COOKIE_PATH)
    return {"detail": "Logged out"}
