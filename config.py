import json
import os
import re

from dotenv import load_dotenv

load_dotenv()

with open("settings.json", "r", encoding="utf-8") as f:
    settings = json.load(f)

BOT_TOKEN = os.getenv('BOT_TOKEN')
CLEAR_LIST = [i for i in re.split(',', os.getenv('ADMIN_IDS')) if i]
ADMIN_IDS = [int(i) for i in CLEAR_LIST]
