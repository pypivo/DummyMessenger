import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from .base import Base

class Messages(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    text = Column(Text)
    counter = Column(Integer, default=0)
    date_creation = Column(DateTime(timezone=True), server_default=func.now())
