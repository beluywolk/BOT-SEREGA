from aiogram import Bot, Dispatcher
from decouple import config
token = config("TOKEN")
bot = Bot(token)
dp = Dispatcher(bot=bot)
photos = ['1.png', '2.png', '3.png', '4.png',
          '5.png', '6.png']