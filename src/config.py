import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env (для локальной разработки)
# load_dotenv()

# Получаем переменные
# В GitHub Actions они будут переданы как environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY") # Изменено имя переменной
DB_PATH = os.getenv("DB_PATH", "data/crm_bot.db")

# Проверка на наличие токена
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("Необходимо указать TELEGRAM_BOT_TOKEN в файле .env или как секрет в GitHub Actions")
# Проверка на наличие API ключа для Gemini
if not GOOGLE_GEMINI_API_KEY: # Изменено имя переменной
    raise ValueError("Необходимо указать GOOGLE_GEMINI_API_KEY в файле .env или как секрет в GitHub Actions")
