from aiogram.dispatcher.filters import CommandStart as _CommandStart
from aiogram.types.message import Message

from src.core import StarterManager


class CommandStart(_CommandStart):
    async def check(self, message: Message):
        starter_id = StarterManager.get_id_from_text(message.text)
        if starter_id is not None:
            return False
        return await super().check(message)