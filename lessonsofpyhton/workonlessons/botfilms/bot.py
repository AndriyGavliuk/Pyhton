from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keybords import *

from films import Films

TOKEN = "6033620263:AAEr9LtA30wY_Ygg0MJy8ueA9fRlbUZRNT8"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Привіт, я рекомендую фільми!", reply_markup=keyboard_inline)


@dp.callback_query_handler()
async def get_film_info(callback_query: types.CallbackQuery):
    if callback_query.data == 'Джон Уік 4 ':
        await bot.send_photo(callback_query.message.chat.id, Films[callback_query.data]["photo"])
        url = Films[callback_query.data]["site_url"]
        film_rating = Films[callback_query.data]["rating"]
        film_description = Films[callback_query.data]["description"]
        message = f"Film url: {url}\nAbout: {film_description}\n\nRate: {film_rating}"
    elif callback_query.data == 'Підземелля і дракони':
        await bot.send_photo(callback_query.message.chat.id, Films[callback_query.data]["photo"])
        url = Films[callback_query.data]["site_url"]
        film_rating = Films[callback_query.data]["rating"]
        film_description = Films[callback_query.data]["description"]
        message = f"Film url: {url}\nAbout: {film_description}\n\nRate: {film_rating}"
    elif callback_query.data == 'Екзорцист Ватикану':
        await bot.send_photo(callback_query.message.chat.id, Films[callback_query.data]["photo"])
        url = Films[callback_query.data]["site_url"]
        film_rating = Films[callback_query.data]["rating"]
        film_description = Films[callback_query.data]["description"]
        message = f"Film url: {url}\nAbout: {film_description}\n\nRate: {film_rating}"


if __name__ == "___main___":
    executor.start_polling(dp)
