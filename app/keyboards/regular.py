from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from .base import RegularKeyboard


class MainMenuKeyboard(RegularKeyboard):
    @classmethod
    def get(cls) -> ReplyKeyboardMarkup:
        keyboard = [
            [KeyboardButton(text="let's start")],
        ]
        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
