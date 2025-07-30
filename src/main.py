import logging
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    CallbackQueryHandler,
    filters
)
from config import TELEGRAM_BOT_TOKEN
from database import init_db
# Импортируем обработчики
import handlers.common_handlers as common_handlers
import handlers.child_handlers as child_handlers
import handlers.parent_handlers as parent_handlers

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Основная функция запуска бота."""
    # Инициализация БД при старте
    init_db()

    # Создание экземпляра Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # --- Регистрация обработчиков ---

    # Диалог выбора роли при старте
    role_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", common_handlers.start)],
        states={
            common_handlers.SELECTING_ROLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, common_handlers.select_role)]
        },
        fallbacks=[CommandHandler("cancel", common_handlers.cancel)],
    )
    application.add_handler(role_conv_handler)

    # ConversationHandler для добавления задач ребёнком
    add_task_conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^📝 Добавить дело$"), child_handlers.add_task)],
        states={
            child_handlers.ADDING_TASK: [MessageHandler(filters.TEXT & ~filters.COMMAND, child_handlers.save_task)]
        },
        fallbacks=[CommandHandler("cancel", common_handlers.cancel)], # Можно использовать общий cancel
    )
    application.add_handler(add_task_conv_handler)

    # ConversationHandler для трекинга настроения ребёнком
    track_mood_conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^🌈 Настроение дня$"), child_handlers.track_mood)],
        states={
            child_handlers.TRACKING_MOOD: [CallbackQueryHandler(child_handlers.save_mood)]
        },
        fallbacks=[CommandHandler("cancel", common_handlers.cancel)],
    )
    application.add_handler(track_mood_conv_handler)

    # Обработчики для ребенка (реагируют на текст кнопок)
    # TODO: Нужно добавить проверку, что пишет именно ребенок
    # application.add_handler(MessageHandler(filters.Regex("^📝 Добавить дело$"), child_handlers.add_task)) # Уже в ConversationHandler
    application.add_handler(MessageHandler(filters.Regex("^✅ Мои дела$"), child_handlers.show_tasks))
    # application.add_handler(MessageHandler(filters.Regex("^🌈 Настроение дня$"), child_handlers.track_mood)) # Уже в ConversationHandler
    application.add_handler(MessageHandler(filters.Regex("^🏆 Мои награды$"), child_handlers.show_rewards))
    application.add_handler(MessageHandler(filters.Regex("^💡 AI-подсказка$"), child_handlers.get_ai_tip))
    application.add_handler(MessageHandler(filters.Regex("^🎮 Челлендж дня$"), child_handlers.get_daily_challenge))

    # Обработчик для родителя (реагирует на callback от inline-кнопок)
    # TODO: Нужно добавить проверку, что нажимает именно родитель
    application.add_handler(CallbackQueryHandler(parent_handlers.parent_callback_handler))

    logger.info("Бот запускается...")
    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
