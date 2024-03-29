import datetime
from hashlib import md5

from sqlalchemy import desc, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func

from .models import Messages


async def add_message(session: AsyncSession, message):
    async with session.begin() as conn:

        await session.execute(text(f"SELECT pg_advisory_xact_lock(('x'||md5('{message.name}'))::bit(64)::bigint);"))

        statement = select(func.max(Messages.counter)).where(Messages.name == message.name)
        rs = await conn.session.execute(statement)
        max_counter = rs.scalar()
        if max_counter is None:
            max_counter = 0

        new_message = Messages(name=message.name, text=message.text, counter=max_counter + 1)
        conn.session.add(new_message)

    return new_message


async def get_messages(session: AsyncSession, limit: int = 10, date = datetime.datetime.now()):
    async with session.begin() as conn:
        statement = select(Messages).limit(limit).where(Messages.date_creation <= date).order_by(desc(Messages.date_creation))
        rs = await conn.session.execute(statement)
        messages = rs.scalars().all()
    return messages

