from aiogram import types, Dispatcher
from config import bot, dp, ADMINS, dice
from random import choice


async def game(message: types.Message):

    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        else:
            await bot.send_dice(message.chat.id, emoji=choice(dice))
async  def go(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не мой босс!")
    else:
        while True:
            await bot.send_message(message.chat.id, '@cgcfmdv чмо')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
    dp.register_message_handler(go, commands=['whoisbaur'])