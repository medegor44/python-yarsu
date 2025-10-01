from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is not None and update.effective_user is not None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')

token = os.getenv("TELEGRAM_TOKEN")
if token is None:
    raise ValueError("TELEGRAM_TOKEN environment variable is not set")

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
