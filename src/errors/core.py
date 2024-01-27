from ._base import Error


class CoreError(Error):
    """Bot core error"""


class RouterError(CoreError):
    """Router error"""


class StarterError(CoreError):
    """
    Starter error

    starter: t.me/bot?start=ID
    """


class UnknownRecorder(RouterError):
    """Unknown recorder for handlers"""
    msg = "Unknown recorder specified"


class RouterDoesNotExist(RouterError):
    """Router was not created in the handler file"""
    msg = "Router not created"


class StarterDoesNotExist(StarterError, RouterError):
    """Attempt to call an unregistered starter-handler"""
    msg = "Starter not created"


class StarterExpired(StarterError):
    """The starter-link has expired"""
    msg = "Link expired"
