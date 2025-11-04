from fastapi import FastAPI, Depends
from app.auth.router import router as auth_router
from app.auth.deps import get_current_user_claims, require_roles
from datetime import datetime, timezone
from fastapi import HTTPException
app = FastAPI(title="Auth Demo (JWT + Refresh Rotation + RBAC)")

# Mount /auth routes
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Auth demo running. See /docs"}

@app.get("/me")
def me(claims: dict = Depends(get_current_user_claims)):
    return {
        "user_id": claims["sub"],
        "roles": claims.get("roles", []),
        "exp": claims.get("exp"),
        "scope": claims.get("scope"),
    }

@app.get("/admin-only")
def admin_only(_: dict = Depends(require_roles(["admin"]))):
    return {"ok": True, "note": "You have admin access!"}

@app.get("/token/status")
def token_status(claims: dict = Depends(get_current_user_claims)):
    now_epoch = int(datetime.now(timezone.utc).timestamp())
    iat = int(claims.get("iat", 0))
    exp = int(claims.get("exp", 0))
    remaining = exp - now_epoch
    return {
        "sub": claims.get("sub"),
        "scope": claims.get("scope"),
        "roles": claims.get("roles", []),
        "issued_at": iat,
        "expires_at": exp,
        "now": now_epoch,
        "seconds_remaining": remaining,
        "about": "Call /auth/refresh to rotate once remaining ~0"
    }

@app.get("/token/require-ttl")
def token_require_ttl(min_seconds: int = 30, claims: dict = Depends(get_current_user_claims)):
    now_epoch = int(datetime.now(timezone.utc).timestamp())
    exp = int(claims.get("exp", 0))
    remaining = exp - now_epoch
    if remaining < min_seconds:
        raise HTTPException(status_code=401, detail=f"Token too close to expiry (< {min_seconds}s). Remaining={remaining}s")
    return {"ok": True, "seconds_remaining": remaining, "min_required": min_seconds}