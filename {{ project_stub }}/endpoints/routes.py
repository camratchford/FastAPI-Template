import logging

from fastapi import APIRouter

from {{ project_stub }}.config import config
from {{ project_stub }}.endpoints.models import Endpoint

logger = logging.getLogger("pymetrics")

router = APIRouter(
    prefix="/api",
    tags=["endpoints"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)
