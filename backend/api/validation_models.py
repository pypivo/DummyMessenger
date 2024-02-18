from enum import Enum
from typing import List

from pydantic import BaseModel


class MessageRequest(BaseModel):
    name: str
    text: str
