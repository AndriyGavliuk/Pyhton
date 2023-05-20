from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from games import gamess


game_choice = InlineKeyboardMarkup()
for game in gamess:
    button = InlineKeyboardButton(text=game, callback_data=game)
game_choice.add(button)
