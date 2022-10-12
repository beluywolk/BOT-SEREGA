import logging
from random import choice
from aiogram import types
from aiogram.utils import executor
from config import bot, dp, photos
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    photo = open(f'memes/1.png', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)
#
#
#
# @dp.message_handler(commands=['meme'])
# async def meme_handler(message: types.Message):
#     photo = open(f'memes/{choice(photos)}', 'rb')
#
#     await bot.send_photo(message.chat.id, photo=photo)
#
#
#
# @dp.message_handler(commands=['prikol'])
# async def q1(message: types.Message):
#     markup = InlineKeyboardMarkup()
#     button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
#     markup.add(button_call_1)
#     question = 'сколько раз я вчера кушал?'
#     answers = ['1', '2', '3', '4', 'глинтвейн', 'завтра']
#     await bot.send_poll(
#         chat_id=message.from_user.id,
#         question=question,
#         options=answers,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=3,
#         explanation='я ел 4 раза',
#         open_period=14,
#         reply_markup=markup
#
#     )
# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
# async def q1(call: types.CallbackQuery):
#
#     question = 'кто убил супермена?'
#     answers = ['Дарксайд', 'Индиана Джонс', 'Бэтмен', 'Думсдэй', 'глинтвейн', 'завтра']
#     await bot.send_poll(
#         chat_id=call.from_user.id,
#         question=question,
#         options=answers,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=3,
#         explanation='я ел 4 раза',
#         open_period=14,
#
#
#     )
#
#
#
# @dp.message_handler()
# async def a(message: types.Message):
#     m = message.text
#     try:
#
#         m = int(m)
#         e = m * m
#         await bot.send_message(message.from_user.id, f'{e}')
#
#     except:
#
#         await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)



