import logging

__all__ = ("setup",)


_LOG_LEVEL = logging.INFO
_LOG_STREAM_FORMAT = (
    "{asctime} | {levelname:^8} | {message}"
)
_LOG_FILE_FORMAT = (
    "{asctime} | {lineno:^3} | {filename:^16} | {levelname:^8} | {message}"
)


def _stream_handler() -> logging.StreamHandler:
    formatter = logging.Formatter(_LOG_STREAM_FORMAT, style="{")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    return handler


def _file_handler() -> logging.FileHandler:
    formatter = logging.Formatter(_LOG_FILE_FORMAT, style="{")

    handler = logging.FileHandler("bot.log", encoding="utf8")
    handler.setFormatter(formatter)

    return handler


log = logging.getLogger()

def setup() -> None:
    log.setLevel(_LOG_LEVEL)
    log.addHandler(_stream_handler())
    log.addHandler(_file_handler())
