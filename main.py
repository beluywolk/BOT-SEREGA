import asyncio
import logging
from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin, anketa, notificationnns
from database.bot_db import sql_create



async def on_startup(_):
    asyncio.create_task(notificationnns.scheduler())
    sql_create()



anketa.register_handlers_anketa(dp)
client.register_hendlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_admin(dp)
notificationnns.register_message_napominalka(dp)



extra.register_hendlers_extra(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



