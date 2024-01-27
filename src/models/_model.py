from typing import Any, Callable, Dict, Generic, Optional, TypeVar

from pydantic import BaseModel

from src.core import MemoryCache, Database
from src.models.id import ID


class Model(BaseModel):
    id: str


ModelT = TypeVar("ModelT", bound=Model)
cache = MemoryCache()


class CRUDMixin(Generic[ModelT]):
    database: Database
    cache_category: str
    callable_model: Callable

    def __init__(self, model: ModelT) -> None:
        self.model = model

    @classmethod
    def _convert_to_model(cls, data: Dict[str, Any]) -> ModelT:
        if "_id" in data:
            id = data.pop("_id")
            data["id"] = id

        return cls.callable_model(**data)

    @classmethod
    def _convert_to_data(cls, model: ModelT) -> Dict[str, Any]:
        data = model.dict()
        if "id" in data:
            id = data.pop("id")
            data["_id"] = id

        return data

    @classmethod
    async def find(cls, id: ID) -> Optional[ModelT]:
        cached_data = cache.get(cls.cache_category, id)
        if cached_data is not None:
            return cls._convert_to_model(cached_data)

        data = await cls.database.db.find_one({"_id": id})
        if data is not None:
            cache.set(cls.cache_category, id, data)
            return cls._convert_to_model(data)

    @classmethod
    async def create(cls, model: ModelT) -> None:
        data = cls._convert_to_data(model)
        await cls.database.db.insert_one(data)
        cache.set(cls.cache_category, model.id, data)

    @classmethod
    async def delete(cls, id: ID) -> None:
        await cls.database.db.delete_one({"_id": id})
        cache.remove(cls.cache_category, id)

    @classmethod
    async def update(cls, id: ID, key: str, value: Any) -> Optional[ModelT]:
        model = await cls.find(id)
        if not model:
            return

        await cls.database.db.update_one({"_id": id}, {"$set": {key: value}})
        setattr(model, key, value)
        cache.set(cls.cache_category, id, cls._convert_to_data(model))
        return model
