from aiogram.dispatcher.filters import IDFilter

from src.config import DEVELOPER_ID


class DeveloperFilter(IDFilter):
    """Filter for the bot developer"""
    def __init__(self) -> None:
        super().__init__(DEVELOPER_ID)
