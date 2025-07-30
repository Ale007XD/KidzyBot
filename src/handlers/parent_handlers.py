from telegram import Update
from telegram.ext import ContextTypes
from ai_module import ai_helper
import logging

# Логирование
logger = logging.getLogger(__name__)

async def parent_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает нажатия на inline-кнопки родителя."""
    query = update.callback_query
    await query.answer() # Обязательно, чтобы убрать "часики" с кнопки
    command = query.data
    user_id = query.from_user.id

    if command == "parent_add_task":
        # TODO: Реализовать диалог добавления задачи для ребенка
        await query.edit_message_text(text="Введите название задачи для ребенка:")
        # Здесь можно установить состояние для ConversationHandler
    elif command == "parent_view_reports":
        # TODO: Сгенерировать и отправить отчет
        # Например: report = generate_report(user_id)
        report = "Отчет по активности ребенка:\n- Задач выполнено: 5/7\n- Настроение: стабильное."
        await query.edit_message_text(text=report)
    elif command == "parent_configure_rewards":
        # TODO: Реализовать интерфейс настройки наград
        await query.edit_message_text(text="Здесь вы сможете настроить награды.")
    elif command == "parent_ai_insights":
        # TODO: Получить и показать AI-рекомендации
        # Например: history = database.get_mood_history(child_id)
        # advice = ai_helper.analyze_mood_data(history) if ai_helper else "..."
        advice = ai_helper.give_parent_advice("Анна", "Выполнила 5 задач") if ai_helper else "AI-помощник не настроен."
        await query.edit_message_text(text=f"🤖 AI-рекомендация: {advice}")
    else:
        await query.edit_message_text(text="Неизвестная команда.")
