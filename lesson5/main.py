from warnings import filters
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler
from dotenv import load_dotenv
from uuid import uuid4
import os
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

load_dotenv()

async def hello(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is not None and update.effective_user is not None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.inline_query is None or update.inline_query.query is None:
        return
    query = update.inline_query.query
    
    results = []
    results.append(
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Caps",
            input_message_content=InputTextMessageContent(
                message_text=f"Caps: {query.upper()}"
            ),
            description=query.upper()
        )
    )

    await context.bot.answer_inline_query(update.inline_query.id, results)


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is not None and update.effective_user is not None:
        await update.message.reply_text(f"Welcome {update.effective_user.first_name}!")

async def get_weather(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is not None:
        await update.message.reply_text("Fetching weather information...")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is not None and update.effective_chat is not None and update.message.text is not None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args is not None and update.message is not None:
        text_caps = ' '.join(context.args).upper()
        await update.message.reply_text(text_caps)

token = os.getenv("TELEGRAM_TOKEN")
if token is None:
    raise ValueError("TELEGRAM_TOKEN environment variable is not set")

app = ApplicationBuilder().token(token).build()

app.add_handler(InlineQueryHandler(inline_caps))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("weather", get_weather))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("caps", caps))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
