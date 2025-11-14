from pydantic import BaseModel, EmailStr
from typing import List

class User(BaseModel):
    id: str
    email: EmailStr
    password_hash: str
    roles: List[str] = ["user"]

class RegisterIn(BaseModel):
    email: EmailStr
    password: str
    roles: List[str] = ["user"]

class LoginIn(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
