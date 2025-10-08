import os
import webbrowser


async def open_url(url):
    """Открывает ссылку в браузере"""
    webbrowser.open(url)


async def shutdown():
    """Выключает ПК"""
    os.system("shutdown -s -t 0 -f")


async def restart():
    """Перезагружает ПК"""
    os.system("shutdown -r -t 0")
