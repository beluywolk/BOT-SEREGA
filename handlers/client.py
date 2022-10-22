from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp, photos
from keyboards.client_kb import start_markup
from random import choice
from database.bot_db import sql_command_random

async def start_handler(message: types.Message):
    await bot.send_message(message.chat.id, f'привет, @{message.from_user.username}, \nкомманды:'
                                            f'\n/start\n/meme\n/prikol\n чтобы закрепить сообщение !pin')





async def meme_handler(message: types.Message):
    photo = open(f'memes/{choice(photos)}', 'rb')

    await bot.send_photo(message.chat.id, photo=photo)




async def q1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)
    question = 'сколько раз я вчера кушал?'
    answers = ['1', '2', '3', '4', 'глинтвейн', 'завтра']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='я ел 4 раза',
        open_period=14,
        reply_markup=markup

    )





def register_hendlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(meme_handler, commands=['meme'])
    dp.register_message_handler(q1, commands=['prikol'])