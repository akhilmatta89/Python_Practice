import os
from datetime import timedelta

# You can set these via environment variables or use defaults
JWT_SECRET = os.getenv("JWT_SECRET", "CHANGE_ME_TO_A_LONG_RANDOM_STRING")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

ACCESS_EXPIRES = timedelta(
    minutes=int(os.getenv("ACCESS_MINUTES", "15"))
)
REFRESH_EXPIRES = timedelta(
    days=int(os.getenv("REFRESH_DAYS", "7"))
)

# Cookie settings for refresh token
REFRESH_COOKIE_NAME = "refresh_token"
REFRESH_COOKIE_PATH = "/auth"
REFRESH_COOKIE_SECURE = True   # set False if testing on pure HTTP (not recommended)
REFRESH_COOKIE_SAMESITE = "strict"
REFRESH_COOKIE_HTTPONLY = True
