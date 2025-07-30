from telegram import Update
from telegram.ext import ContextTypes
from ai_module import ai_helper

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Что нужно сделать? Напиши мне.")

async def show_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Вот твои дела на сегодня: \n- Почистить зубы 🔁\n- Сделать уроки")

async def track_mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Как твое настроение сегодня? Расскажи мне!")

async def show_rewards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("У тебя 150 XP! Твой уровень: 2. \nДоступные награды: ...")

async def get_ai_tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if ai_helper:
        tip = ai_helper.get_idea_for_child("творчество")
        await update.message.reply_text(f"💡 Идея дня: {tip}")
    else:
        await update.message.reply_text("Извини, мой AI-помощник сейчас отдыхает.")
