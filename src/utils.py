from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

CHILD_MAIN_MENU_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["📝 Добавить дело", "✅ Мои дела"],
        ["🌈 Настроение дня", "🏆 Мои награды"],
        ["💡 AI-подсказка", "🎮 Челлендж дня"],
    ],
    resize_keyboard=True
)

def get_parent_main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("➕ Добавить задачу ребенку", callback_data="parent_add_task")],
        [InlineKeyboardButton("📊 Посмотреть отчеты", callback_data="parent_view_reports")],
        [InlineKeyboardButton("🎁 Настроить награды", callback_data="parent_configure_rewards")],
        [InlineKeyboardButton("🤖 AI-рекомендации", callback_data="parent_ai_insights")],
    ]
    return InlineKeyboardMarkup(keyboard)
