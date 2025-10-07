from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_panel():
    btn_pc_shutdown = InlineKeyboardButton(text="Выключить", callback_data='btn_pc_shutdown')
    btn_pc_restart = InlineKeyboardButton(text="Перезагрузить", callback_data='btn_pc_restart')
    # btn_pc_open_link = InlineKeyboardButton(text="Открыть ссылку", callback_data='btn_pc_open_link')
    kb = InlineKeyboardBuilder().row(btn_pc_shutdown, btn_pc_restart, width=2)
    return kb
