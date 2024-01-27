from aiogram import Bot as AIOgramBot

from src.config import TOKEN
from src.triggers import core as triggers

from .dispatcher import Dispatcher


class Bot(AIOgramBot):
    def __init__(self):
        self.dp = Dispatcher(self)
        super().__init__(TOKEN, parse_mode="HTML")

    def load_routers(self):
        triggers.loading_routers.notify()
        self.dp.register_routers()

    async def run(self):
        triggers.starting_bot.notify(await self.me)
        await self.dp.start_polling()
