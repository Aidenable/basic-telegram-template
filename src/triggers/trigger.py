import logging
from typing import Callable, List, Optional

log = logging.getLogger()


class Trigger:
    def __init__(
        self,
        triggers: List[Callable] = [],
        *,
        log_msg: Optional[str] = None,
        log_level: int = logging.INFO
    ):
        self.triggers = triggers
        self.log_msg = log_msg
        self.log_level = log_level

    def create(self, callable: Callable):
        self.triggers.append(callable)

    def notify(self, *args, **kwargs):
        if self.log_msg is not None:
            log.log(
                self.log_level, self.log_msg.format(*args, **kwargs)
            )

        for trigger in self.triggers:
            trigger(*args, **kwargs)
