from telegram import Update
from telegram.ext import ContextTypes

async def parent_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    command = query.data
    
    if command == "parent_add_task":
        await query.edit_message_text(text="Введите название задачи для ребенка:")
    elif command == "parent_view_reports":
        await query.edit_message_text(text="Отчет по активности ребенка: \n- Задач выполнено: 5/7\n- Настроение: стабильное.")
    elif command == "parent_configure_rewards":
        await query.edit_message_text(text="Здесь вы сможете настроить награды.")
    elif command == "parent_ai_insights":
        await query.edit_message_text(text="AI-рекомендация: Похвалите ребенка за успехи в учебе!")
    else:
        await query.edit_message_text(text="Неизвестная команда.")
