from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

from bot.keyboard import markups as kb
from bot.tools.decorators import admin_only
from core.system_control import open_url, restart, shutdown

router = Router()


@router.message(Command(commands=["s", "start"]))
async def command_start(message: Message):
    # text = settings["startup_message"].format(id=id)
    await message.answer(
        f"Ку"
    )


@router.message(Command(commands=["admin"]))
@admin_only
async def command_open(message: Message):
    await message.answer(
        "Админ панель",
        reply_markup=kb.admin_panel().as_markup()
    )


@router.message(Command(commands=["sd", "shutdown"]))
@admin_only
async def command_shutdown(message: Message):
    await message.answer(
        "Выключаю компьютер"
    )
    await shutdown()


@router.message(Command(commands=["r", "restart"]))
@admin_only
async def command_restart(message: Message):
    await message.answer(
        "Перезагружаю компьютер"
    )
    await restart()


@router.message(Command(commands=["o", "open"]))
@admin_only
async def command_open(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer(
            "Укажи ссылку: /open https://example.com"
        )
        return
    url = args[1]
    await message.answer(
        f"Открываю: {url}"
    )
    await open_url(url)
