import logging
import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN, LANGUAGES
from news_parser import get_triggers
from lang import get_text

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

user_langs = {}  # Store user language preferences

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["English", "Русский"]]
    await update.message.reply_text(
        "Choose your language / Выберите язык:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    lang = user_langs.get(user_id, 'en')
    triggers = get_triggers()
    if not triggers:
        await update.message.reply_text(get_text("no_alerts", lang))
    else:
        msg = get_text("alerts", lang) + "\n\n" + "\n\n".join(triggers)
        await update.message.reply_text(msg)

async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang_text = update.message.text.lower()
    user_id = update.message.from_user.id
    if lang_text in LANGUAGES:
        user_langs[user_id] = LANGUAGES[lang_text]
        await update.message.reply_text(get_text("welcome", LANGUAGES[lang_text]))
    else:
        await update.message.reply_text("Invalid language / Неверный язык")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, set_language))

    logger.info("Bot is running...")
    app.run_polling()