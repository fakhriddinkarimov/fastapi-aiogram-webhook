import logging
from aiogram import executor, Dispatcher

from data.config import WEBHOOK_URL
from loader import bot, dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher: Dispatcher) -> None:
    # Webhookni tekshirish
    webhook_info = await dispatcher.bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)
        
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher: Dispatcher) -> None:
    await dispatcher.bot.delete_webhook()
    await dispatcher.bot.close()
    await dispatcher.storage.close()
    logging.getLogger(__name__).info("Bot to'xtadi")
    

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
