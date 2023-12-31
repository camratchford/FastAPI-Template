import logging

from fastapi import Depends, FastAPI

from {{ project_stub }}.config import config

from {{ project_stub }}.db import create_db_and_tables

from {{ project_stub }}.users.user import auth_backend, current_active_user, fastapi_users
from {{ project_stub }}.users.schemas import UserRead, UserCreate, UserUpdate
from {{ project_stub }}.users.models import User

from {{ project_stub }}.endpoints.routes import router as endpoints_router

config.configure_basic_logging()
config.configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(name="{{ project_name }}")
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
    await create_db_and_tables()

@app.get("/")
async def root():
    return {200: "{{ project_name }} API is working"}