import sqlite3
import os
from config import DB_PATH

def init_db():
    """Инициализирует базу данных и создает таблицы, если их нет."""
    # Убедимся, что директория для БД существует
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Таблица пользователей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        role TEXT NOT NULL, -- 'child', 'parent', 'mentor'
        parent_id INTEGER, -- для связи ребенка с родителем
        xp INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1
    )''')

    # Таблица задач
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT NOT NULL,
        description TEXT, -- Добавлено описание задачи
        xp_reward INTEGER DEFAULT 10,
        is_recurring BOOLEAN DEFAULT FALSE,
        recurring_type TEXT, -- 'daily', 'weekdays', etc.
        status TEXT DEFAULT 'pending', -- 'pending', 'completed'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )''')

    # Таблица отслеживания настроения
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mood_tracker (
        mood_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        mood_score INTEGER NOT NULL, -- например, от 1 до 5
        comment TEXT,
        tracked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )''')

    # Таблица наград (пример)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rewards (
        reward_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        cost INTEGER NOT NULL -- Стоимость в XP
    )''')

    # Таблица достижений (пример)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS achievements (
        achievement_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT NOT NULL,
        description TEXT,
        earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )''')

    conn.commit()
    conn.close()
    print("База данных успешно инициализирована.")

def add_user(user_id, role, parent_id=None):
    """Добавляет нового пользователя в БД."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (user_id, role, parent_id) VALUES (?, ?, ?)",
                   (user_id, role, parent_id))
    conn.commit()
    conn.close()

# TODO: Добавить функции для работы с задачами, настроением, отчетами и т.д.
# Например:
# def get_user_role(user_id):
# def add_task(user_id, title, description, xp_reward, is_recurring, recurring_type):
# def get_tasks_for_user(user_id):
# def track_mood(user_id, mood_score, comment):
# def get_mood_history(user_id):
# def get_user_xp(user_id):
# def award_xp(user_id, xp_amount):
# def get_available_rewards():
# def purchase_reward(user_id, reward_id):
