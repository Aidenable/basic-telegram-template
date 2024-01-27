from aiogram.types import Message, ContentTypes
from aiogram.dispatcher.filters import (
    CommandHelp, CommandSettings, CommandPrivacy,
    ContentTypeFilter, ForwardedMessageFilter
)

from src.ext.filters import CommandStart
from src.core import Router

router = Router("content")


@router.message(CommandStart())
async def start(message: Message):
    await message.reply("Start")

@router.message(CommandHelp())
async def help(message: Message):
    await message.reply("Help")

@router.message(CommandSettings())
async def settings(message: Message):
    await message.reply("Settings")

@router.message(CommandPrivacy())
async def privacy(message: Message):
    await message.reply("Privacy")

@router.message(ContentTypeFilter(ContentTypes.PHOTO | ContentTypes.DOCUMENT))
async def media(message: Message):
    await message.reply("Photo or Document")

@router.message(ForwardedMessageFilter(True))
async def forwarded(message: Message):
    await message.reply(message.forward_from.get_mention(as_html=True))
