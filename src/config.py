import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DB_PATH = os.getenv("DB_PATH", "data/crm_bot.db")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("Необходимо указать TELEGRAM_BOT_TOKEN в файле .env")
