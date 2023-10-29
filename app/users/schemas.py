import datetime
import uuid

from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser):
    first_name: str
    last_name: str


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str]
    last_name: Optional[str]
