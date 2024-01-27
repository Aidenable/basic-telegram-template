from logging import getLogger
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient

from src.config import MONGO_NAME, MONGO_TOKEN

log = getLogger()


class Database:
    def __init__(
        self,
        collection: str,
        database: Optional[str] = None
    ) -> None:
        if database is None:
            database = MONGO_NAME

        self._client = AsyncIOMotorClient(MONGO_TOKEN)
        self._database = self._client.get_database(database)
        self.db = self._database.get_collection(collection)
