from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton

kb_help_for_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_help_for_start.add(KeyboardButton("/help"))