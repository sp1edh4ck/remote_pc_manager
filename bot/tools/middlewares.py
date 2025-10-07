from aiogram import BaseMiddleware

import config


class AdminOnlyMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user_id = event.from_user.id
        if user_id in config.ADMIN_IDS:
            return await handler(event, data)
        else:
            await event.answer("🚫 У тебя нет доступа к этой команде.")
            return
