from typing import Dict, Optional
from app.auth.models import User
from app.core.security import hash_password

# In-memory stores
USERS_BY_EMAIL: Dict[str, User] = {}
USERS_BY_ID: Dict[str, User] = {}

def create_user(email: str, password: str, roles: list[str]) -> User:
    if email in USERS_BY_EMAIL:
        raise ValueError("Email already registered")
    new_id = str(len(USERS_BY_ID) + 1)
    user = User(
        id=new_id,
        email=email,
        password_hash=hash_password(password),
        roles=roles or ["user"],
    )
    USERS_BY_EMAIL[email] = user
    USERS_BY_ID[new_id] = user
    return user

def get_user_by_email(email: str) -> Optional[User]:
    return USERS_BY_EMAIL.get(email)

def get_user_by_id(user_id: str) -> Optional[User]:
    return USERS_BY_ID.get(user_id)
