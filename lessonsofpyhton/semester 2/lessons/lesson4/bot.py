from weather import parse_weather
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "6033620263:AAEr9LtA30wY_Ygg0MJy8ueA9fRlbUZRNT8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Hello i am echo bot!")
    await message.answer("Hello i am echo bot!")


@dp.message_handler(content_types="text")
async def get_weather(message: types.Message):
    world_weather = parse_weather(city=message.text)
    min_temperature = round(world_weather['main']['temp_min'] - 273, 2)
    max_temperature = round(world_weather["main"]["temp_max"] - 273, 2)
    temperature = round(world_weather["main"]["temp"] - 273, 2)
    wind_speed = round(world_weather['wind']['speed'] * 3.6, 2)
    await message.answer(f"Погода у місті {message.text}. Мінімальна температура:{min_temperature}, максимальна температура: {max_temperature}, температура: {temperature}, а швидкість вітра {wind_speed}")

# @dp.message_handler(text="Погода")
# async def weather(message: types.Message):
#     await message.answer("Погода сьогодні дуже приємна, чи не так?")


# @dp.message_handler()
# async def echo(message: types.Message):
#     user_info = {
#         "name": message.from_user.first_name,
#         "surname": message.from_user.last_name,
#         "username": message.from_user.username,
#         "user_id": message.from_user.id
#     }
#     await message.answer(f'First name: {user_info["name"]}\nLast name: {user_info["surname"]}\nUsername: {user_info["username"]}\nUser id: {user_info["user_id"]}')
#     await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp)
