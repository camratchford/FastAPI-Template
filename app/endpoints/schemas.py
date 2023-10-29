from typing import Optional

from pydantic import BaseModel


class EndpointSchema(BaseModel):
    id: Optional[int]
    hostname: str