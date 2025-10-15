from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, InlineQueryHandler
import logging
from uuid import uuid4

from WeatherHandler import WeatherHandler
from WeatherApiService import WeatherApiService

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.message is not None
    assert update.effective_user is not None

    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.message is not None
    assert context is not None and context.args is not None and len(context.args) >= 3

    await update.message.reply_text('Calculating...')
    a = float(context.args[0])
    op = context.args[1]
    b = float(context.args[2])

    match op:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/':
            result = a / b if b != 0 else 'Division by zero error'
        case _:
            result = 'Invalid operator'

    await update.message.reply_text(f'Result: {result}')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.message is not None
    assert update.message.text is not None

    await update.message.reply_text(update.message.text.upper())

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.inline_query is not None

    query = update.inline_query.query
    if not query:
        return
    
    results = []
    results.append(
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper()),
            description="Convert text to uppercase"
        )
    )
    results.append(
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Reversed",
            input_message_content=InputTextMessageContent(query[::-1]),
            description="Convert text to reversed",
        )
    )

    await context.bot.answer_inline_query(update.inline_query.id, results)

handler = WeatherHandler(WeatherApiService())

app = ApplicationBuilder().token("8459132623:AAEEKFRtNp9hf_qmzps9_fismKgm5a9UBd0").build()

app.add_handler(InlineQueryHandler(caps))
app.add_handler(CommandHandler("weather", handler.get_weather))
app.add_handler(CommandHandler("forecast", handler.get_weather_forecast))
app.add_handler(MessageHandler(filters.LOCATION, handler.get_weather_by_location))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("calc", calculate))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()