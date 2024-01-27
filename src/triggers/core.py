from logging import getLogger

from .trigger import Trigger

log = getLogger()

starting_bot = Trigger(
    log_msg="Starting...",
    triggers=[
        lambda bot: log.info(f"Bot: {bot.full_name} [{bot.id}]")
    ]
)

loading_routers = Trigger()

loading_router = Trigger(
    [lambda router: log.info(f"Loading handler: {router.name}")])
loading_starter = Trigger(
    [lambda starter: log.info(f"Loading starter: {starter}")])

register_handler = Trigger()
