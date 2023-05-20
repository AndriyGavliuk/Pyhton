from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from films import films

film_choice = InlineKeyboardMarkup()
for film in films:
    button = InlineKeyboardButton(text=film, callback_data=film)
    film_choice.add(button)
