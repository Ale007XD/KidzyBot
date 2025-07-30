from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# --- Клавиатуры для Ребёнка (ReplyKeyboardMarkup) ---
CHILD_MAIN_MENU_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["📝 Добавить дело", "✅ Мои дела"],
        ["🌈 Настроение дня", "🏆 Мои награды"],
        ["💡 AI-подсказка", "🎮 Челлендж дня"],
    ],
    resize_keyboard=True
)

# --- Клавиатуры для Родителя (InlineKeyboardMarkup) ---
def get_parent_main_menu_keyboard():
    """Возвращает клавиатуру главного меню для родителя."""
    keyboard = [
        [InlineKeyboardButton("➕ Добавить задачу ребенку", callback_data="parent_add_task")],
        [InlineKeyboardButton("📊 Посмотреть отчеты", callback_data="parent_view_reports")],
        [InlineKeyboardButton("🎁 Настроить награды", callback_data="parent_configure_rewards")],
        [InlineKeyboardButton("🤖 AI-рекомендации", callback_data="parent_ai_insights")],
    ]
    return InlineKeyboardMarkup(keyboard)

# TODO: Добавить другие клавиатуры по мере необходимости
# Например, клавиатура для выбора настроения (эмодзи)
def get_mood_keyboard():
    """Возвращает клавиатуру для выбора настроения."""
    keyboard = [
        [InlineKeyboardButton("😄 Отлично", callback_data="mood_5"),
         InlineKeyboardButton("😊 Хорошо", callback_data="mood_4")],
        [InlineKeyboardButton("😐 Нормально", callback_data="mood_3"),
         InlineKeyboardButton("😔 Плохо", callback_data="mood_2")],
        [InlineKeyboardButton("😢 Ужасно", callback_data="mood_1")],
    ]
    return InlineKeyboardMarkup(keyboard)
