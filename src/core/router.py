from typing import Any, Callable, Dict, List, Optional, Union

from aiogram import Dispatcher
from aiogram.types import Message, ContentType

from src.errors import StarterDoesNotExist, UnknownRecorder
from src.triggers import core as triggers


class RouterHandler:
    def __init__(
        self,
        recorder: str,
        callback: Callable[[Any], Any],
        *args: Any,
        **kwargs: Any
    ):
        self.recorder = recorder
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def register(self, dispatcher: Dispatcher):
        recorder = getattr(dispatcher, f"register_{self.recorder}_handler")

        if recorder is None:
            raise UnknownRecorder

        recorder(self.callback, *self.args, **self.kwargs)


class Router:
    _starters: Dict[str, Callable] = {}

    def __init__(self, name: Optional[str] = None):
        self.name = name
        self._handlers: List[RouterHandler] = []

        self.chat_join_request = self._decorator_factory("chat_join_request")
        self.chat_member = self._decorator_factory("chat_member")
        self.my_chat_member = self._decorator_factory("my_chat_member")
        self.poll = self._decorator_factory("poll")
        self.poll_answer = self._decorator_factory("poll_answer")
        self.pre_checkout_query = self._decorator_factory("pre_checkout_query")
        self.shipping_query = self._decorator_factory("shipping_query")
        self.inline = self._decorator_factory("inline")
        self.chosen_inline = self._decorator_factory("chosen_inline")
        self.channel_post = self._decorator_factory("channel_post")
        self.edited_channel_post = self._decorator_factory(
            "edited_channel_post")

    def _decorator_factory(self, recorder: str) -> Callable:
        def handler(
            *args: Any, **kwargs: Any
        ) -> Callable[[Callable[[Any], Any]], Callable[[Any], Any]]:
            def decorator(
                callback: Callable[[Any], Any]
            ) -> Callable[[Any], Any]:
                self._handlers.append(
                    RouterHandler(recorder, callback, *args, **kwargs)
                )
                return callback
            return decorator
        return handler

    def command(self, commands: Union[List[str], str], *filters, **kwargs) -> Callable:
        if isinstance(commands, str):
            commands = [commands]

        def decorator(callback: Callable) -> Callable:
            self._handlers.append(RouterHandler(
                "message",
                callback,
                commands=commands,
                *filters,
                **kwargs
            ))
            return callback
        return decorator

    def message(
        self, 
        *filters, 
        regexp: Optional[str] = None, 
        content_types: Optional[ContentType] = None, 
        **kwargs
    ) -> Callable:
        def decorator(callback: Callable) -> Callable:
            self._handlers.append(RouterHandler(
                "message",
                callback,
                *filters,
                regexp=regexp,
                content_types=content_types,
                **kwargs
            ))
            return callback
        return decorator

    def edited_message(
        self, 
        *filters, 
        regexp: Optional[str] = None, 
        content_types: Optional[ContentType] = None, 
        **kwargs
    ) -> Callable:
        def decorator(callback: Callable) -> Callable:
            self._handlers.append(RouterHandler(
                "edited_message",
                callback,
                *filters,
                regexp=regexp,
                content_types=content_types,
                **kwargs
            ))
            return callback
        return decorator

    def errors(
        self, 
        *filters, 
        exception: Optional[Exception] = None,  
        **kwargs
    ) -> Callable:
        def decorator(callback: Callable) -> Callable:
            self._handlers.append(RouterHandler(
                "errors",
                callback,
                *filters,
                exception=exception,
                **kwargs
            ))
            return callback
        return decorator

    def callback_query(
        self, 
        *filters,
        text: Optional[str] = None,
        **kwargs
    ) -> Callable:
        def decorator(callback: Callable) -> Callable:
            self._handlers.append(RouterHandler(
                "callback_query",
                callback,
                *filters,
                text=text,
                **kwargs
            ))
            return callback
        return decorator

    @property
    def handlers(self) -> List[RouterHandler]:
        return self._handlers

    def starter(self, starter_name: str) -> Callable:
        def wrapper(callback: Callable[[Any], Any]) -> Callable[[Any], Any]:
            triggers.loading_starter.notify(starter_name)
            self._starters[starter_name] = callback
            return callback
        return wrapper

    @classmethod
    async def trigger_starter(
        cls,
        starter_name: str,
        message: Message,
        *args: Any,
        **kwargs
    ) -> None:
        if starter_name not in cls._starters:
            raise StarterDoesNotExist

        await cls._starters[starter_name](message, *args, **kwargs)
