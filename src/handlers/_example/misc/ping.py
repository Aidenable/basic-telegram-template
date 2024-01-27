from aiogram.types import Message

from src.core import Router

router = Router("ping")


@router.command("ping")
async def ping(message: Message):
    await message.reply("Pong!")
