from datetime import datetime, timezone
from typing import Any, Optional, Dict
import uuid
import jwt

from .config import JWT_SECRET, JWT_ALGORITHM, ACCESS_EXPIRES, REFRESH_EXPIRES

def _now() -> datetime:
    return datetime.now(timezone.utc)

def create_token(sub: str, scope: str, expires_seconds: int, extra: Optional[Dict[str, Any]] = None) -> str:
    iat = int(_now().timestamp())
    payload: Dict[str, Any] = {"sub": sub, "scope": scope, "iat": iat, "exp": iat + expires_seconds}
    if extra:
        payload.update(extra)
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def create_access_token(user_id: str, roles: list[str]) -> str:
    return create_token(
        sub=user_id,
        scope="access",
        expires_seconds=int(ACCESS_EXPIRES.total_seconds()),
        extra={"roles": roles}
    )

def create_refresh_token(user_id: str) -> tuple[str, str]:
    tid = str(uuid.uuid4())
    token = create_token(
        sub=user_id,
        scope="refresh",
        expires_seconds=int(REFRESH_EXPIRES.total_seconds()),
        extra={"tid": tid}
    )
    return token, tid
