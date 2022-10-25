import asyncio

import aioschedule
from aiogram import types, Dispatcher
from config import bot

async def privet(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('привет')


async def snova_privet():
    await bot.send_message(chat_id=chat_id, text='о, привет, а я тебя знаю')


async def scheduler():
    aioschedule.every().friday.at('10:00').do(snova_privet)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(3)



def register_message_napominalka(dp: Dispatcher):
    dp.register_message_handler(privet, lambda word: 'поздоровайся' in word.text)