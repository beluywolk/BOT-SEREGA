import logging
from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin

client.register_hendlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_admin(dp)
extra.register_hendlers_extra(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)



