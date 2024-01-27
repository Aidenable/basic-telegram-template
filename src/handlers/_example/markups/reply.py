from aiogram.types import Message

from src.core import Router
from src.markups.example_reply import EXAMPLE_REPLY_CALLBACK, example_reply

router = Router("reply")


@router.command("reply")
async def reply(message: Message):
    await message.reply("Reply", reply_markup=example_reply)

@router.message(text=EXAMPLE_REPLY_CALLBACK)
async def example_reply(message: Message):
    await message.reply("Reply Example 1")
