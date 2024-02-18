from fastapi import APIRouter, Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import get_db
from db.services import add_message, get_messages
from .validation_models import MessageRequest

message_router = APIRouter(prefix="/messages")

@message_router.post('')
async def add_messages(message: MessageRequest, session: AsyncSession = Depends(get_db)):
    new_message = await add_message(session, message)
    messages = await get_messages(session, date=new_message.date_creation)
    return messages