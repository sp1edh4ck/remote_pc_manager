from aiogram import Router
from aiogram.types import CallbackQuery

from bot.keyboard import markups as kb
from bot.tools.decorators import admin_only
from core.system_control import open_url, restart, shutdown

router = Router()


@router.callback_query(lambda call: call.data == "btn_pc_shutdown")
@admin_only
async def btn_pc_shutdown(call: CallbackQuery):
    await call.answer(
        "Выключаю компьютер"
    )
    await shutdown()


@router.callback_query(lambda call: call.data == "btn_pc_shutdown")
@admin_only
async def btn_pc_shutdown(call: CallbackQuery):
    await call.answer(
        "Перезагружаю компьютер"
    )
    await restart()


@router.callback_query(lambda call: call.data == "btn_pc_shutdown")
@admin_only
async def btn_pc_shutdown(call: CallbackQuery):
    args = call.text.split(maxsplit=1)
    if len(args) < 2:
        await call.answer(
            "Укажи ссылку: /open https://example.com"
        )
        return
    url = args[1]
    await call.answer(
        f"Открываю: {url}"
    )
    await open_url(url)
