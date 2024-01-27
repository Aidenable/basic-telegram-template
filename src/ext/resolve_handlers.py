from os import listdir, path
from pathlib import Path
from typing import List, Union

__all__ = ("resolve_handlers",)


def _resursive(directory: Union[str, Path], files: List[str]):
    for file_name in listdir(directory):
        file_path = Path(directory, file_name)

        if file_name.startswith("_"):
            continue

        if path.isfile(file_path) and file_name.endswith(".py"):
            files.append(str(file_path))
        elif path.isdir(file_path):
            _resursive(file_path, files)


def resolve_handlers(
    categories: List[str],
    root: Union[str, Path, None] = None
) -> List[str]:
    handlers = []

    if isinstance(root, str):
        root = Path(*root.split("."))

    for category in categories:
        item = category

        if root is not None:
            item = Path(root, category)

        if path.isdir(item):
            _resursive(item, handlers)
            continue

        if not category.endswith(".py"):
            item = Path(root or "", category + ".py")

        if path.isfile(item):
            handlers.append(item)

    return handlers
