from aiogram import Bot, Dispatcher
from decouple import config
token = config("TOKEN")
bot = Bot(token)
dp = Dispatcher(bot=bot)
photos = ['download.png', 'e06e76e5c12c911b545070f6374795a4.jpg', 'Emp3KzaW4AMUfLK.jpg', 'maxresdefault.jpg',
          'mqdefault.jpg']