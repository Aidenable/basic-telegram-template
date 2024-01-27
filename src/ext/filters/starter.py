from re import compile
from aiogram.dispatcher.filters import CommandStart

from src.core import StarterManager


class StarterFilter(CommandStart):
    """Filter for starter-links such as t.me/BOT?start=ID."""
    def __init__(self):
        super().__init__(
            compile(StarterManager.PREFIX + r'[\w-]+'),
            False
        )
