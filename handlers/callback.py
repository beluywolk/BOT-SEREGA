from config import dp, bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton





async def q2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    markup.add(button_call_1)

    question = 'кто убил супермена?'
    answers = ['Дарксайд', 'Индиана Джонс', 'Бэтмен', 'Думсдэй', 'глинтвейн', 'завтра']
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='вот так)',
        open_period=14,
        reply_markup=markup


    )
async def q3(call: types.CallbackQuery):


    question = 'почему собаки гавкают?'
    answers = ['незнаю', 'потому что вот', 'они не гавкают', 'й', 'глинтвейн', 'завтра']
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='вот так вот)',
        open_period=14



    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(q2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(q3, lambda call: call.data == "button_call_2")