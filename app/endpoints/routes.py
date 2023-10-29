import logging

from fastapi import APIRouter, Depends

from app.config import config
from app.db import get_async_session
from app.endpoints.models import Endpoint
from app.endpoints.schemas import EndpointSchema


logger = logging.getLogger("pymetrics")

router = APIRouter(
    prefix="/api",
    tags=["endpoints"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/parents/", response_model=EndpointSchema)
async def read_endpoint(endpoint: EndpointSchema):
    async with get_async_session() as sess:
        target_endpoint = sess.get(Endpoint, **endpoint.model_dump())
        yield target_endpoint