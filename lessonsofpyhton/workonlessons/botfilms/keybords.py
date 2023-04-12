from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
button1 = InlineKeyboardButton(text="Джон Уік 4", callback_data="John Week")
button2 = InlineKeyboardButton(
    text="Підземелля і дракони ", callback_data="Підземелля і дракони ")
button3 = InlineKeyboardButton(
    text="Екзорцист Ватикану ", callback_data="Екзорцист Ватикану ")

keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)
