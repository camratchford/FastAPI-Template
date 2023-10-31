
from sqlalchemy import Column, ForeignKey, Integer, String

from {{ project_stub }}.db import Base


class Endpoint(Base):
    __tablename__ = "Endpoints"
    id = Column(Integer, primary_key=True)
    hostname = Column(String)