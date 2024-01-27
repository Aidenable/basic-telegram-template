from aiogram.types import Message

from src.core import Router, StarterManager
from src.ext.filters import StarterFilter

router = Router("starter")


@router.message(StarterFilter())
async def start(message: Message):
    starter_id = StarterManager.get_id_from_text(message.text)
    if starter_id is not None:
        return await StarterManager.trigger(starter_id, message)

@router.command("myid")
async def myid(message: Message):
    await message.reply(
        await StarterManager.get(
            (await message.bot.get_me()).username, 
            "starter-handler", 
            message.from_id
        )
    )

@router.starter("starter-handler")
async def starter_handler(message: Message, from_id: int):
    await message.reply(str(from_id))
