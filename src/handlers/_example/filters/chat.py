from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import ChatTypeFilter

from src.core import Router

router = Router("chat")


@router.command("only_pm", ChatTypeFilter(ChatType.PRIVATE))
async def only_pm(message: Message):
    await message.reply("Only PM")

@router.command("only_group", ChatTypeFilter(ChatType.GROUP))
async def only_group(message: Message):
    await message.reply("Only group")
