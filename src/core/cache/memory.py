from datetime import datetime, timedelta
from typing import Any, Union


class MemoryCache:
    _storage = {}

    def get(self, category: str, key: Any) -> Any:
        if category not in self._storage or key not in self._storage[category]:
            return
        return self._storage[category][key]["data"]

    def get_by_sub(self, category: str, sub_value: Any) -> Any:
        if category not in self._storage:
            return

        for key, value in self._storage[category]:
            for sub_obj in value:
                sub_data = sub_obj['data']
                if sub_value in sub_data:
                    return self._storage[category][key]

    def set(
        self,
        category: str,
        key: Any,
        value: Any,
        expire: Union[float, timedelta] = 60  # 7200
    ):
        if category not in self._storage:
            self._storage[category] = {}

        if isinstance(expire, (float, int)):
            expire = timedelta(seconds=expire)

        self._storage[category][key] = {
            "data": value,
            "expire": expire,
            "created_at": datetime.now()
        }

    def remove_category(self, category: str):
        self._storage.pop(category)

    def remove(self, category: str, key: Any):
        if category not in self._storage or key not in self._storage[category]:
            return
        self._storage[category].pop(key)
