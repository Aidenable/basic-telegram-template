from ._keyboard import InlineKeyboardMarkup, InlineKeyboardButton


EXAMPLE_INLINE_CALLBACK = "example-1"
EXAMPLE2_INLINE_CALLBACK = "example-2"

example_inline = InlineKeyboardMarkup()

example_inline.add(
    InlineKeyboardButton("Example", callback_data=EXAMPLE_INLINE_CALLBACK),
    InlineKeyboardButton("Example 2", callback_data=EXAMPLE2_INLINE_CALLBACK),
)