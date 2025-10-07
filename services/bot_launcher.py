from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

import config
from bot.handlers import callbacks, commands


async def start_bot():
    try:
        bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
        dp = Dispatcher()
        await bot.delete_webhook(drop_pending_updates=True)
        dp.include_router(callbacks.router)
        dp.include_router(commands.router)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
