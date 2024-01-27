from aiogram.types import ChatAdministratorRights
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.core.bot import Bot
from src.core.logger import setup as logger_setup
from src.ext.schedulers.cache_cleaner import cache_cleaner
from src.ext.schedulers.starter_cleaner import starter_cleaner

scheduler = AsyncIOScheduler()
bot = Bot()


def _schedule_interval_jobs():
    scheduler.add_job(starter_cleaner, "interval", minutes=30)
    scheduler.add_job(cache_cleaner, 'interval', hours=1)


async def setup():
    logger_setup()
    _schedule_interval_jobs()

    bot.load_routers()
    await bot.set_my_default_administrator_rights(
        ChatAdministratorRights(  # type: ignore
            can_delete_messages=True,
            can_post_messages=True,
            can_edit_messages=True,
        )
    )

    scheduler.start()
    await bot.run()
