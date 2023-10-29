import logging

from fastapi import Depends, FastAPI


from app.config import config
from app.defaults import swagger_ui_config

from app.db import create_db_and_tables

from app.users.user import auth_backend, current_active_user, fastapi_users
from app.users.schemas import UserRead, UserCreate, UserUpdate
from app.users.models import User

from app.endpoints.routes import router as endpoints_router

config.configure_basic_logging()
config.configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI-Template", swagger_ui_parameters=swagger_ui_config)
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
app.include_router(endpoints_router)

config.app = app


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()

@app.get("/")
async def root():
    return {200: "working"}