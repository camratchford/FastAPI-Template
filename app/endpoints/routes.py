import logging

from fastapi import APIRouter

from app.config import config
from app.endpoints.models import Endpoint

logger = logging.getLogger("pymetrics")

router = APIRouter(
    prefix="/api",
    tags=["endpoints"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)
