from WeatherApiService import WeatherApiService, Weather
from telegram import Update
from telegram.ext import ContextTypes

class WeatherHandler:
    def __init__(self, service: WeatherApiService):
        self._service = service

    async def get_weather_by_location(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
        assert update.message is not None
        assert update.message.location is not None

        coords = update.message.location

        weather = await self._service.get_weather_coords(coords.latitude, coords.longitude)
        await self.reply_weather(str((coords.latitude, coords.longitude)), weather, update)

    async def get_weather_forecast(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
        assert ctx.args is not None
        assert update.message is not None
        assert len(ctx.args) >= 1

        city = ctx.args[0]

        weatherForecast = await self._service.get_weather_forecast(city)

        reply = []
        for forecast in weatherForecast.forecast: # type: ignore
            (dt, weather) = forecast
            reply.append(f"The weather at {dt} is {weather.weather} temp: {weather.temp}, feels like {weather.feels_like}")

        await update.message.reply_text('\n'.join(reply)) # type: ignore


    async def get_weather(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
        assert ctx.args is not None
        assert update.message is not None
        assert len(ctx.args) >= 1

        city = ctx.args[0]

        weather = await self._service.get_weather(ctx.args[0])

        await self.reply_weather(city, weather, update)


    async def reply_weather(self, location: str, weather: Weather | None, update: Update):
        if weather:
            await update.message.reply_text( # type: ignore
                f"The weather in {location} is {weather.weather} temp: {weather.temp}, feels like {weather.feels_like}"
            )
        else:
            await update.message.reply_text(F"The weather in {location} is unknown") # type: ignore