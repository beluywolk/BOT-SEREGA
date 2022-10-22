from aiogram import types, Dispatcher

from config import bot, dp


async def echo(message: types.Message):


    m = message.text
    if m.startswith('!'):
        if not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

def register_hendlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
