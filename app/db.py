import logging

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


from app.config import config


class Base(DeclarativeBase):
    pass


engine = create_async_engine(config.sql_alchemy_uri)
# async_session_maker = async_sessionmaker(engine, expire_on_commit=True, autoflush=True)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker(engine, expire_on_commit=True, autoflush=True)() as session:
        yield session






