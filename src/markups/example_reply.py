from ._keyboard import ReplyKeyboardMarkup, ReplyKeyboardButton


EXAMPLE_REPLY_CALLBACK = "Example"
EXAMPLE2_REPLY_CALLBACK = "Example 2"

example_reply = ReplyKeyboardMarkup(resize_keyboard=True)

example_reply.add(
    ReplyKeyboardButton(EXAMPLE_REPLY_CALLBACK),
    ReplyKeyboardButton(EXAMPLE2_REPLY_CALLBACK),
)