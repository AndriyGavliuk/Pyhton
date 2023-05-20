import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6033620263:AAEr9LtA30wY_Ygg0MJy8ueA9fRlbUZRNT8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    # await bot.send_message(message.from_user.id, "Hello i am echo bot!")
    await message.answer("Hello i am echo bot!")


@dp.message_handler(text="Погода")
async def weather(message: types.Message):
    await message.answer("Погода сьогодні дуже приємна, чи не так?")


if __name__ == "___main___":
    executor.start_polling(dp)
