from asyncio import run

from services.bot_launcher import start_bot

if __name__ == "__main__":
    run(start_bot())
