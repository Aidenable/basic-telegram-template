from aiogram.types import Message
from aiogram.dispatcher.filters import AdminFilter
from aiogram.dispatcher.filters.filters import OrFilter

from src.core import Router
from src.ext.filters import DeveloperFilter, OwnerFilter, WhitelistFilter

router = Router("user")


@router.command("check_admin", AdminFilter(is_chat_admin=True))
async def check_admin(message: Message):
    await message.reply("Admin")

@router.command("check_owner", OwnerFilter())
async def check_owner(message: Message):
    await message.reply("Owner")

@router.command("check_dev", DeveloperFilter())
async def check_dev(message: Message):
    await message.reply("Developer")

@router.command("check_stuff", OrFilter(AdminFilter(), DeveloperFilter()))
async def check_stuff(message: Message):
    await message.reply("Stuff")

@router.command("check_whitelist", WhitelistFilter([1, 2, 3, 4]))
async def check_whitelist(message: Message):
    await message.reply("Whitelist")
