from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
token = config("TOKEN")
bot = Bot(token)
dp = Dispatcher(bot=bot, storage=storage)
photos = ['photo_5377843858764840531_y.jpg', 'download.png', 'e06e76e5c12c911b545070f6374795a4.jpg', 'Emp3KzaW4AMUfLK.jpg', 'maxresdefault.jpg', 'mqdefault.jpg']
ADMINS = [804372471]
dice = ['🎰', '🎳', '🎯', '🎲', '🏀', '⚽']