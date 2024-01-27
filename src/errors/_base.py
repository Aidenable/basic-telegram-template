from typing import Union


class Error(Exception):
    msg: str = "An error has occured"

    def __init__(
        self,
        message: Union[str, None] = None,
        *args
    ) -> None:
        if message is not None:
            self.msg = message

        super().__init__(self.msg, *args)
