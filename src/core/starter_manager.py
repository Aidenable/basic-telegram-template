from typing import Optional
from datetime import datetime
from uuid import uuid4

from aiogram.types import Message

from src.core.router import Router
from src.errors import StarterExpired

from .cache import MemoryCache
from .database import Database

starterDB = Database('Starter')
cache = MemoryCache()


class StarterManager:
    PREFIX = r"RR_"

    @classmethod
    def get_id_from_text(cls, text: str) -> Optional[str]:
        parts = text.split()
        if len(parts) < 2:
            return
        
        if parts[-1].startswith(cls.PREFIX):
            return parts[-1]
        return text.split("?start=")[-1]

    @classmethod
    async def get(cls, bot_username: str, handler: str, *args) -> str:
        id = str(uuid4())
        starter_object = {
            "_id": id,
            "handler": handler,
            "args": args,
            "created_at": datetime.now()
        }
        await starterDB.db.insert_one(starter_object)
        cache.set("starters", id, starter_object)
        return f"t.me/{bot_username}?start={cls.PREFIX}{id}"

    @classmethod
    async def trigger(cls, id: str, message: Message) -> None:
        if not id.startswith(cls.PREFIX):
            return

        data = cache.get('starters', id[3:])
        if data is None:
            data = await starterDB.db.find_one({"_id": id[3:]})
            if not data:
                raise StarterExpired

        await Router.trigger_starter(data["handler"], message, *data["args"])

    @classmethod
    async def finish(cls, id: str) -> None:
        cache.remove('starters', id)
        await starterDB.db.delete_one({"_id": id})
