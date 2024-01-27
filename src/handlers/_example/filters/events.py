from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import ChatTypeFilter

from src.core import Router

router = Router("events")


@router.message(ChatTypeFilter(ChatType.GROUP), regexp=r"^[^\/].*")
async def on_group_message(message: Message):
    await message.reply(message.text)

@router.errors(exception=ZeroDivisionError)
async def on_error(message: Message):
    await message.reply("0/0 = 4")
