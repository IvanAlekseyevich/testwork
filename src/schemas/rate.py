# from datetime import datetime
# from typing import Optional, List

from pydantic import BaseModel

# from .base import DBObjectBase


# class Base64Image(BaseModel):
#     filename: str
#     base64: str
#
#
# class ChatCreateRequest(BaseModel):
#     title: str = Field(..., min_length=1, max_length=100)
#     logo: Optional[Base64Image] = None

class Rate(BaseModel):
    cargo_type: str
    rate: float

# class Rates(DBObjectBase):
#     id: int
#     title: str
#     avatar_chat: Optional[str]
#     is_active: bool
#     is_project_chat: bool
#     date_create: datetime
#
#
# class AllChatsResponse(BaseModel):
#     count: int
#     chats: Optional[List[CurrentChatResponse]]
