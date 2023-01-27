from beanie import init_beanie
from fastapi import Depends, FastAPI

from app.db import db
from app.manager.users import current_active_user
from app.models.user import User

app = FastAPI()
from .routes import router as base_router

app.include_router(base_router)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.on_event("startup")
async def on_startup():
    await init_beanie(
        database=db,
        document_models=[
            User,
        ],
    )
