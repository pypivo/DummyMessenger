import datetime

from sqlalchemy import desc, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func

from .models import Messages


async def max_counter_lock(session, message):
    statement = select(Messages).where(
        (Messages.counter == select(func.max(Messages.counter))) & (Messages.name == message.name) )
    rs = await session.execute(statement)
    message_with_max_counter: Messages = rs.scalar()
    if message_with_max_counter is not None:
        await session.execute(text(f'SELECT pg_advisory_xact_lock({message_with_max_counter.id})'))


async def add_message(session: AsyncSession, message):
    async with session.begin() as conn:

        await max_counter_lock(session=conn.session, message=message)
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

