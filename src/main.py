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
from handlers import common_handlers, child_handlers, parent_handlers
from handlers.common_handlers import SELECTING_ROLE

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    init_db()
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    role_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", common_handlers.start)],
        states={
            SELECTING_ROLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, common_handlers.select_role)]
        },
        fallbacks=[CommandHandler("cancel", common_handlers.cancel)],
    )
    application.add_handler(role_conv_handler)
    
    application.add_handler(MessageHandler(filters.Regex("^📝 Добавить дело$"), child_handlers.add_task))
    application.add_handler(MessageHandler(filters.Regex("^✅ Мои дела$"), child_handlers.show_tasks))
    application.add_handler(MessageHandler(filters.Regex("^🌈 Настроение дня$"), child_handlers.track_mood))
    application.add_handler(MessageHandler(filters.Regex("^🏆 Мои награды$"), child_handlers.show_rewards))
    application.add_handler(MessageHandler(filters.Regex("^💡 AI-подсказка$"), child_handlers.get_ai_tip))

    application.add_handler(CallbackQueryHandler(parent_handlers.parent_callback_handler))

    logger.info("Бот запускается...")
    application.run_polling()

if __name__ == "__main__":
    main()
