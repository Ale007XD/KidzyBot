import sqlite3
import os
from config import DB_PATH

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        role TEXT NOT NULL,
        parent_id INTEGER,
        xp INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT NOT NULL,
        xp_reward INTEGER DEFAULT 10,
        is_recurring BOOLEAN DEFAULT FALSE,
        recurring_type TEXT,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mood_tracker (
        mood_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        mood_score INTEGER NOT NULL,
        comment TEXT,
        tracked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )''')

    conn.commit()
    conn.close()
    print("База данных успешно инициализирована.")

def add_user(user_id, role, parent_id=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (user_id, role, parent_id) VALUES (?, ?, ?)",
                   (user_id, role, parent_id))
    conn.commit()
    conn.close()
