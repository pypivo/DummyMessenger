from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import settings


engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=True)

async def get_db() -> AsyncGenerator:
    async with async_session() as session:
        yield session
