from datetime import datetime

from src.core import MemoryCache

cache = MemoryCache()


async def cache_cleaner():
    now = datetime.now()
    categories = cache._storage.items()

    for category_name, cache_items in categories:
        items = cache_items.copy().items()
        for item_name, item in items:
            if item["created_at"] + item["expire"] >= now:
                cache.remove(category_name, item_name)
