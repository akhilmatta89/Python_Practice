from datetime import datetime, timezone
from typing import Any, Optional, Dict
import uuid
import jwt

from .config import JWT_SECRET, JWT_ALGORITHM, ACCESS_EXPIRES, REFRESH_EXPIRES

def _now() -> datetime:
    return datetime.now(timezone.utc)

def _exp(delta) -> int:
    return int((_now() + delta).timestamp())

def create_token(sub: str, scope: str, expires_sec: int, extra: Optional[Dict[str, Any]] = None) -> str:
    payload: Dict[str, Any] = {
        "sub": sub,
        "scope": scope,
        "iat": int(_now().timestamp()),
        "exp": int(_now().timestamp()) + expires_sec,
    }
    if extra:
        payload.update(extra)
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def create_access_token(user_id: str, roles: list[str]) -> str:
    return create_token(
        sub=user_id,
        scope="access",
        expires_sec=int(ACCESS_EXPIRES.total_seconds()),
        extra={"roles": roles}
    )

def create_refresh_token(user_id: str) -> tuple[str, str]:
    tid = str(uuid.uuid4())
    token = create_token(
        sub=user_id,
        scope="refresh",
        expires_sec=int(REFRESH_EXPIRES.total_seconds()),
        extra={"tid": tid}
    )
    return token, tid
