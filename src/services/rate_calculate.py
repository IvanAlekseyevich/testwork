import sqlalchemy as sa

from src.chat.crud import get_db
from src.chat.enums import UserRoleEnum
from src.chat.models import ChatRoom, ChatRoomAdmins, ChatRoomUser
from src.chat.schemas import JwtUserSchema


# async def is_chat_user(chat_id: int, user_id: int):
#     q = (
#         sa.select(ChatRoomUser.chatroom_id)
#         .where(ChatRoomUser.chatroom_id == chat_id)
#         .where(ChatRoomUser.user_id == user_id)
#     )
#     async with get_db() as db:
#         current_chat = (await db.execute(q)).scalar()
#     if current_chat is None:
#         return False
#     else:
#         return True

