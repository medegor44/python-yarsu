import os

class EnvVariableProvider:
    @staticmethod
    def get_telegram_token() -> str | None:
        return os.getenv("TELEGRAM_TOKEN")

    @staticmethod
    def get_open_weather_token() -> str | None:
        return os.getenv("OPEN_WEATHER_TOKEN")
