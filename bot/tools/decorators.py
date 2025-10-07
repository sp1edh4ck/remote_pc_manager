from functools import wraps

from aiogram.types import Message

import config


def admin_only(handler):
    @wraps(handler)
    async def wrapper(message: Message, *args, **kwargs):
        if message.from_user.id in config.ADMIN_IDS:
            return await handler(message, *args, **kwargs)
        else:
            return
    return wrapper
