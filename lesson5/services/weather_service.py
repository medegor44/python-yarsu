import aiohttp

from services.weather import Weather
from utils.env_variable_provider import EnvVariableProvider

class WeatherService:
    def __init__(self, env_var_provider: EnvVariableProvider) -> None:
        self._api_key = env_var_provider.get_open_weather_token()
        if not self._api_key:
            raise ValueError("API key is missing")
        

    async def get_weather(self, city: str) -> Weather | None:
        coordinates = await self._get_city_coordinates(city)
        if not coordinates:
            return None

        (lat, lon) = coordinates

        params = {
            'lat': lat,
            'lon': lon,
            'appid': self._api_key,
            'units': 'metric'
        }
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.openweathermap.org/data/2.5/weather', params=params, ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    try:
                        return Weather(
                            temp=data['main']['temp'],
                            weather=data['weather'][0]['main'],
                            temp_feels_like=data['main']['feels_like']
                        )
                    except KeyError:
                        return None
                return None

    async def _get_city_coordinates(self, city: str) -> tuple[float, float] | None:
        params = {
            'q': city,
            'limit': 1,
            'appid': self._api_key
        }
        async with aiohttp.ClientSession() as session:
            async with session.get('http://api.openweathermap.org/geo/1.0/direct', params=params, ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    try:
                        return (data[0]['lat'], data[0]['lon']) if data and len(data) > 0 else None
                    except (KeyError, IndexError):
                        return None
