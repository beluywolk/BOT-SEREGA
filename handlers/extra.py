from aiogram import types, Dispatcher
from random import choice

from config import bot, dp, ADMINS


async def echo(message: types.Message):
    m = message.text

    if m.startswith('!'):
        if not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        mgs = [f'мать твоя {message.text}', 'пошел ты', f'{message.text} у тебя в штанах', f'ты черт и '
                                                                                           f'{message.text} тоже черт']
        if message.from_user.id in ADMINS:
            await bot.send_message(message.chat.id, 'здравстуйте, босс, вы очень красивы сегодня', reply_to_message_id=message.message_id)
        else:
            await bot.send_message(message.chat.id, choice(mgs), reply_to_message_id=message.message_id)

def register_hendlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
