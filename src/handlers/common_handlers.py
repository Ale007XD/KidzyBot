from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
from database import add_user
from utils import CHILD_MAIN_MENU_KEYBOARD, get_parent_main_menu_keyboard

SELECTING_ROLE = 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет, {user.mention_html()}! Я твой помощник в мире дел и приключений. ✨"
        "\n\nКто ты?",
        reply_markup=ReplyKeyboardMarkup([["Я Ребёнок 🧒"], ["Я Родитель 🧑‍👩‍👧"]], one_time_keyboard=True, resize_keyboard=True)
    )
    return SELECTING_ROLE

async def select_role(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.effective_user.id
    role_text = update.message.text

    if "Ребёнок" in role_text:
        role = "child"
        add_user(user_id, role)
        await update.message.reply_text(
            "Отлично! Теперь ты можешь добавлять дела, следить за настроением и получать награды!",
            reply_markup=CHILD_MAIN_MENU_KEYBOARD
        )
    elif "Родитель" in role_text:
        role = "parent"
        add_user(user_id, role)
        await update.message.reply_text(
            "Добро пожаловать! Вы можете добавлять задачи для ребенка и следить за его прогрессом.",
            reply_markup=get_parent_main_menu_keyboard()
        )
    else:
        await update.message.reply_text("Пожалуйста, выбери один из вариантов на клавиатуре.")
        return SELECTING_ROLE

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Действие отменено.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
