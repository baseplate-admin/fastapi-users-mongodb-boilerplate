from fastapi import APIRouter
from .auth import router as auth_router
from .auth.jwt import router as jwt_router
from .users import router as user_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(jwt_router)
router.include_router(user_router)
