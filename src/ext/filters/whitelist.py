from typing import List, Dict, Any, Optional, Union

from aiogram.types import Message, CallbackQuery, InlineQuery, ChatMemberUpdated
from aiogram.dispatcher.filters import Filter


class WhitelistFilter(Filter):
    """Filter for users on the allowed list"""
    def __init__(self, whitelist: List[int]) -> None:
        self.whitelist: List[int] = whitelist

    @classmethod
    def validate(cls, full_config: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        result = {}
        if 'whitelist' in full_config:
            result['whitelist'] = full_config.pop('whitelist')
        return result

    async def check(self, obj: Union[Message, CallbackQuery, InlineQuery, ChatMemberUpdated]):
        if isinstance(obj, Message):
            user_id = None
            if obj.from_user is not None:
                user_id = obj.from_user.id
        elif isinstance(obj, CallbackQuery):
            user_id = obj.from_user.id
        elif isinstance(obj, InlineQuery):
            user_id = obj.from_user.id
        elif isinstance(obj, ChatMemberUpdated):
            user_id = obj.from_user.id
        else:
            return False

        return user_id in self.whitelist
