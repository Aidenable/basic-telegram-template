from datetime import datetime, timedelta

from src.core import StarterManager, starterDB


async def starter_cleaner():
    now = datetime.now()
    starters = starterDB.db.find()

    async for starter in starters:
        starter_dt = starter.get("created_at", now)
        if starter_dt + timedelta(minutes=15) <= now:
            await StarterManager.finish(starter["_id"])
