from typing import Optional

from src.core import MemoryCache, Database
from src.models._model import CRUDMixin, Model

title = "example"
exampleDB = Database(title)
cache = MemoryCache()


class ExampleModel(Model):
    example_data_1: bool
    example_data_2: Optional[str] = None


class Example(CRUDMixin[ExampleModel]):
    database = exampleDB
    cache_category = title
    callable_model = ExampleModel

    @classmethod
    async def find_by_data_1(cls, example_data_1: bool) -> Optional[ExampleModel]:
        """Additional method."""
        cache_data = cache.get_by_sub(cls.cache_category, example_data_1)
        if cache_data is not None:
            return ExampleModel(**cache_data)

        data = await cls.database.db.find_one({"example_data_1": example_data_1})
        if data is not None:
            model = ExampleModel(**data)
            cache.set(cls.cache_category, model.id, data)
            return model
