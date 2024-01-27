from typing import Union

from aiogram.types import (
    Message, CallbackQuery, InlineQuery, 
    ChatMemberUpdated, ChatMemberOwner, ChatType
)
from aiogram.dispatcher.filters import AdminFilter


class OwnerFilter(AdminFilter):
    """Filter for the group chat owner"""
    async def check(self, obj: Union[Message, CallbackQuery, InlineQuery, ChatMemberUpdated]) -> bool:
        user_id = obj.from_user.id

        if self._check_current:
            if isinstance(obj, Message):
                chat = obj.chat
            elif isinstance(obj, CallbackQuery) and obj.message:
                chat = obj.message.chat
            elif isinstance(obj, ChatMemberUpdated):
                chat = obj.chat
            else:
                return False
            if chat.type == ChatType.PRIVATE:  # there is no admin in private chats
                return False
            chat_ids = [chat.id]
        else:
            chat_ids = self._chat_ids

        admins = [member.user.id for chat_id in chat_ids 
                  for member in await obj.bot.get_chat_administrators(chat_id) if isinstance(member, ChatMemberOwner)]

        return user_id in admins
