from aiogram.types import Message, InlineQuery

from src.core import Router
from src.markups.example_inline import example_inline, EXAMPLE2_INLINE_CALLBACK

router = Router("inline")


@router.command("inline")
async def inline(message: Message):
    await message.reply("Inline", reply_markup=example_inline)

@router.callback_query(text=EXAMPLE2_INLINE_CALLBACK)
async def example_callback(query: InlineQuery):
    await query.message.reply("Inline Example 2")
