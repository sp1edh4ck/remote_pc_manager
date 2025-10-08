from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import config


def main_menu(user_id):
    kb = InlineKeyboardBuilder()
    if user_id in config.ADMIN_IDS:
        btn_admin_panel = InlineKeyboardButton(text="Админ панель", callback_data='btn_admin_panel')
        kb.row(btn_admin_panel)
    btn_a = InlineKeyboardButton(text="А", callback_data='btn_a')
    kb.row(btn_a)
    return kb


def admin_panel():
    btn_pc_shutdown_menu = InlineKeyboardButton(text="Меню выключения", callback_data='btn_pc_shutdown_menu')
    btn_pc_restart_menu = InlineKeyboardButton(text="Меню рестарта", callback_data='btn_pc_restart_menu')
    # btn_pc_open_link = InlineKeyboardButton(text="Открыть ссылку", callback_data='btn_pc_open_link')
    kb = InlineKeyboardBuilder().row(btn_pc_shutdown_menu, btn_pc_restart_menu, width=2)
    return kb


def shutdown_menu():
    btn_pc_shutdown = InlineKeyboardButton(text="Выключить сразу", callback_data='btn_pc_shutdown')
    btn_pc_shutdown_timer = InlineKeyboardButton(text="Выключить по таймеру", callback_data='btn_pc_shutdown_timer')
    btn_back_admin_panel = InlineKeyboardButton(text="Назад", callback_data='btn_back_admin_panel')
    kb = InlineKeyboardBuilder().row(btn_pc_shutdown, btn_pc_shutdown_timer, btn_back_admin_panel, width=1)
    return kb
