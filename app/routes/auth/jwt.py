from fastapi import APIRouter
from app.manager.users import fastapi_users, auth_backend

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
