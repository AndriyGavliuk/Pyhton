import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import os

# from games import gamess

TOKEN = '6283649322:AAG2BXJoPSyplZOfvCq3EDOUnk-B634oyr0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

ADMINS = [1573130205]


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(text="Привіт, я бот Чашка! Обери гру на свій смак!\nВикористай команду /genres для вибору жанра.")

genres = '/genres'


@dp.message_handler(commands='genres')
async def start(message: types.Message):

    kb = [

        [types.KeyboardButton("Пригодницькі🏕")],
        [types.KeyboardButton("Шутери🔫")],
        [types.KeyboardButton("Бої🤜🤛")],
        [types.KeyboardButton("Гонки🏎")],
        [types.KeyboardButton("Стратегії♟️")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True, selective=True)
    await message.answer('Який жанр ігор тобі подобається?', reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def start(message: types.Message):
    if (message.text == "Пригодницькі🏕"):
        await message.answer("Ось які ігри я раджу в жанрі Пригодницьці.🏕")

        adventure = {
            1: 'Slime rancher 2: https://store.steampowered.com/app/1657630/Slime_Rancher_2/',
            2: 'Hogwarts Legacy: https://www.hogwartslegacy.com/uk-ua ',
            3: 'Terraria: https://www.hogwartslegacy.com/uk-ua',
            4: 'Elden Ring: https://store.steampowered.com/agecheck/app/1245620/',
            5: 'The Elder Scrolls V Skyrim: https://elderscrolls.bethesda.net/ru/skyrim'
        }
        await message.answer(f'1: {adventure[1]}\n2: {adventure[2]}\n3: {adventure[3]}\n4: {adventure[4]}\n5: {adventure[5]}')

    if (message.text == "Шутери🔫"):
        await message.answer("Ось які ігри я раджу в жанрі Шутери.🔫")

        shooters = {
            1: 'Call of Duty:MW: https://store.steampowered.com/agecheck/app/1938090/',
            2: 'Counter Strike GO: https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/',
            3: 'Battlefield: https://store.steampowered.com/franchise/Battlefield?l=russian',
            4: 'Shatterline: https://www.shatterline.gg',
            5: 'Fortnite: https://www.fortnite.com '
        }
        await message.answer(f'1: {shooters[1]}\n2: {shooters[2]}\n3: {shooters[3]}\n4: {shooters[4]}\n5: {shooters[5]}')

    if (message.text == "Бої🤜🤛"):
        await message.answer("Ось які ігри я раджу в жанрі Бої.🤜🤛")

        fights = {
            1: 'Mortal Combat X: https://store.steampowered.com/agecheck/app/307780/',
            2: 'WWE2k: https://wwe.2k.com   ',
            3: 'Hellish Quart: https://store.steampowered.com/app/1000360/Hellish_Quart/ ',
            4: 'For Honor: https://www.ubisoft.com/ru-ru/game/for-honor',
            5: 'Sclash: https://store.steampowered.com/app/1284130/Sclash/ '
        }
        await message.answer(f'1: {fights[1]}\n2: {fights[2]}\n3: {fights[3]}\n4: {fights[4]}\n5: {fights[5]}')

    if (message.text == "Гонки🏎"):
        await message.answer("Ось які ігри я раджу в жанрі Гонки.🏎")

        race = {
            1: 'Need for Speed MW: https://store.steampowered.com/app/1262560/Need_for_Speed_Most_Wanted/',
            2: 'Forza Horizon: https://forza.net ',
            3: 'DiRT: https://dirtgame.com/uk ',
            4: 'Drift Racing Online : https://store.steampowered.com/app/635260/CarX_Drift_Racing_Online/',
            5: 'Asphalt 9: https://store.steampowered.com/app/1815780/Asphalt_9_Legends/'
        }
        await message.answer(f'1: {race[1]}\n2: {race[2]}\n3: {race[3]}\n4: {race[4]}\n5: {race[5]}')

    if (message.text == "Стратегії♟️"):
        await message.answer("Ось які ігри я раджу в жанрі Стратегії.♟️")

        strategy = {
            1: "Sid Meier's Civilization 6: https://store.steampowered.com/app/289070/Sid_Meiers_Civilization_VI/",
            2: 'StarCraft II: https://starcraft2.com/ru-ru/ ',
            3: 'Warcraft III: Reforged: https://playwarcraft3.com/ru-ru/ ',
            4: 'Heroes of Might and Magic: https://store.ubisoft.com/us/might-and-magic/',
            5: 'Age of Mythology: https://www.ageofempires.com/games/aom/ '
        }
        await message.answer(f'1: {strategy[1]}\n2: {strategy[2]}\n3: {strategy[3]}\n4: {strategy[4]}\n5: {strategy[5]}')


if __name__ == '__main__':
    executor.start_polling(dp)
