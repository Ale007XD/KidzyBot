from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from ai_module import ai_helper
from utils import get_mood_keyboard
import logging

# Логирование
logger = logging.getLogger(__name__)

# Состояния для ConversationHandler
ADDING_TASK, TRACKING_MOOD = range(2)

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Начинает диалог добавления задачи."""
    await update.message.reply_text("Что нужно сделать? Напиши мне.")
    return ADDING_TASK

async def save_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Сохраняет новую задачу."""
    user_id = update.effective_user.id
    task_title = update.message.text
    # TODO: Сохранить задачу в БД
    # Например: database.add_task(user_id, task_title)
    logger.info(f"Пользователь {user_id} добавил задачу: {task_title}")
    await update.message.reply_text(f"Задача '{task_title}' добавлена!")
    # Вернуться в главное меню
    from utils import CHILD_MAIN_MENU_KEYBOARD # Импорт внутри, чтобы избежать циклического импорта
    await update.message.reply_text("Выбери действие:", reply_markup=CHILD_MAIN_MENU_KEYBOARD)
    return ConversationHandler.END

async def show_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показывает список активных задач."""
    user_id = update.effective_user.id
    # TODO: Получить задачи из БД и отобразить
    # Например: tasks = database.get_tasks_for_user(user_id)
    tasks = ["Почистить зубы 🔁", "Сделать уроки"] # Заглушка
    if tasks:
        task_list = "\n".join([f"- {task}" for task in tasks])
        message = f"Вот твои дела на сегодня:\n{task_list}"
    else:
        message = "У тебя пока нет активных дел. Добавь новое!"
    await update.message.reply_text(message)

async def track_mood(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Начинает диалог отслеживания настроения."""
    await update.message.reply_text("Как твое настроение сегодня?", reply_markup=get_mood_keyboard())
    return TRACKING_MOOD

async def save_mood(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Сохраняет настроение."""
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    mood_score = int(query.data.split('_')[1]) # Извлекаем оценку из callback_data

    # TODO: Сохранить настроение в БД
    # Например: database.track_mood(user_id, mood_score, "")
    logger.info(f"Пользователь {user_id} отметил настроение: {mood_score}")

    await query.edit_message_text(text=f"Спасибо! Ты отметил настроение: {mood_score}/5.")
    # Вернуться в главное меню
    from utils import CHILD_MAIN_MENU_KEYBOARD
    await query.message.reply_text("Выбери действие:", reply_markup=CHILD_MAIN_MENU_KEYBOARD)
    return ConversationHandler.END

async def show_rewards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показывает награды."""
    user_id = update.effective_user.id
    # TODO: Получить данные о наградах и XP из БД
    # Например: xp = database.get_user_xp(user_id)
    xp = 150 # Заглушка
    level = 2 # Заглушка
    # Например: rewards = database.get_available_rewards()
    rewards = ["_EXTRA_LIFE_", "Пятёрка по любимому предмету", "30 минут игр"] # Заглушка
    reward_list = "\n".join([f"- {reward}" for reward in rewards])
    message = f"У тебя {xp} XP! Твой уровень: {level}.\nДоступные награды:\n{reward_list}"
    await update.message.reply_text(message)

async def get_ai_tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Дает AI-подсказку."""
    if ai_helper:
        tip = ai_helper.get_idea_for_child("творчество") # Можно сделать выбор категории
        await update.message.reply_text(f"💡 Идея дня: {tip}")
    else:
        await update.message.reply_text("Извини, мой AI-помощник сейчас отдыхает.")

async def get_daily_challenge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показывает ежедневный челлендж."""
    if ai_helper:
        challenge = ai_helper.suggest_daily_challenge()
        await update.message.reply_text(f"🎮 Челлендж дня: {challenge}")
    else:
        await update.message.reply_text("Извини, мой AI-помощник сейчас отдыхает.")
