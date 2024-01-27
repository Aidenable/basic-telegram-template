from typing import List, Optional

from aiogram.types import (
    ReplyKeyboardMarkup as _ReplyKeyboardMarkup, 
    KeyboardButton as _KeyboardButton,
    InlineKeyboardMarkup as _InlineKeyboardMarkup,
    InlineKeyboardButton as _InlineKeyboardButton,
    KeyboardButtonPollType, WebAppInfo, LoginUrl,
    CallbackGame,
)

__all__ = ("ReplyKeyboardMarkup", "ReplyKeyboardButton", "InlineKeyboardMarkup", "InlineKeyboardButton",)


def ReplyKeyboardMarkup(
    keyboard: List[List[_KeyboardButton]] = [], 
    resize_keyboard: bool = False,
    one_time_keyboard: bool = False,
    input_field_placeholder: Optional[str] = None,
    selective: bool = False,
    row_width: int = 3,
) -> _ReplyKeyboardMarkup:
    return _ReplyKeyboardMarkup(
        keyboard=keyboard, 
        resize_keyboard=resize_keyboard,
        one_time_keyboard=one_time_keyboard,
        input_field_placeholder=input_field_placeholder,
        selective=selective,
        row_width=row_width,
    ) # type: ignore

def ReplyKeyboardButton(
    text: str,
    request_contact: bool = False,
    request_location: bool = False,
    request_poll: Optional[KeyboardButtonPollType] = None,
    web_app: Optional[WebAppInfo] = None,
) -> _KeyboardButton:
    return _KeyboardButton(
        text=text,
        request_contact=request_contact,
        request_location=request_location,
        request_poll=request_poll,
        web_app=web_app,
    ) # type: ignore

def InlineKeyboardMarkup(row_width: int = 3) -> _InlineKeyboardMarkup:
    return _InlineKeyboardMarkup(row_width=row_width) # type: ignore

def InlineKeyboardButton(
    text: str,
    url: Optional[str] = None,
    login_url: Optional[LoginUrl] = None,
    callback_data: Optional[str] = None,
    switch_inline_query: Optional[str] = None,
    switch_inline_query_current_chat: Optional[str] = None,
    callback_game: Optional[CallbackGame] = None,
    pay: bool = False,
    web_app: Optional[WebAppInfo] = None, 
) -> _InlineKeyboardButton:
    return _InlineKeyboardButton(
        text=text,
        url=url,
        login_url=login_url,
        callback_data=callback_data,
        switch_inline_query=switch_inline_query,
        switch_inline_query_current_chat=switch_inline_query_current_chat,
        callback_game=callback_game,
        pay=pay,
        web_app=web_app,
    ) # type: ignore