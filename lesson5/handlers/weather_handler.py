from services.weather_service import WeatherService
from telegram import Update
from telegram.ext import ContextTypes

class WeatherHandler:
    def __init__(self, weather_service: WeatherService) -> None:
        self._weather_service = weather_service

    async def get_weather(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
        assert update.message is not None
        assert ctx.args is not None
        assert len(ctx.args) > 0

        city = ctx.args[0]
        if city is None:
            await update.message.reply_text("Please provide a city name.")
            return

        weather = await self._weather_service.get_weather(city)
        if weather:
            await update.message.reply_text(f"Weather in {city}: {weather.temp}°C, {weather.weather}")
        else:
            await update.message.reply_text(f"Could not retrieve weather for {city}.")
