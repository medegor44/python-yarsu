from aiohttp import ClientSession
import datetime

class Weather:
    def __init__(self, temp: float, feels_like: float, weather: str):
        self._temp = temp
        self._feels_like = feels_like
        self._weather = weather
    
    @property
    def temp(self):
        return self._temp
    
    @property
    def feels_like(self):
        return self._feels_like
    
    @property
    def weather(self):
        return self._weather
    
class WeatherForecast:
    def __init__(self, forecast: list[tuple[datetime.datetime, Weather]]):
        self._forecast = forecast

    @property
    def forecast(self):
        return self._forecast

class WeatherApiService:
    def __init__(self):
        self._base_url = "https://api.openweathermap.org"
        self._api_key = "a61be5ab67b3846421f70273ab7335e7"
    
    async def get_city_location(self, city_name: str) -> tuple[float, float] | None:
        params = {
            "q": city_name,
            "limit": 1,
            "appid": self._api_key
        }
        async with ClientSession() as session:
            async with session.get(f"{self._base_url}/geo/1.0/direct", params=params, ssl=False) as response:
                if response.status == 200:
                    resp = await response.json()
                    if resp is None or len(resp) == 0:
                        return None
                    lat = resp[0]['lat']
                    lon = resp[0]['lon']

                    return (lat, lon)
                
        return None
    
    async def get_weather_coords(self, lat: float, lon: float) -> Weather | None:
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self._api_key,
            "units": "metric"
        }

        async with ClientSession() as session:
            async with session.get(f"{self._base_url}/data/2.5/weather", params=params, ssl=False) as response:
                if response.status == 200:
                    resp = await response.json()

                    try:
                        weather = resp["weather"][0]["main"]
                        temp = resp["main"]["temp"]
                        feels_like = resp["main"]["feels_like"]

                        return Weather(temp, feels_like, weather)
                    except KeyError:
                        return None
        return None
    
    async def get_weather_forecast_coords(self, lat: float, lon: float) -> WeatherForecast | None:
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self._api_key,
            "units": "metric"
        }

        async with ClientSession() as session:
            async with session.get(f"{self._base_url}/data/2.5/forecast", params=params, ssl=False) as response:
                if response.status == 200:
                    resp = await response.json()
                    
                    forecast = []
                    try:
                        for weatherResponse in resp["list"]:
                            weather = weatherResponse["weather"][0]["main"]
                            temp = weatherResponse["main"]["temp"]
                            feels_like = weatherResponse["main"]["feels_like"]
                            dt = weatherResponse["dt"]

                            forecast.append((
                                datetime.datetime.fromtimestamp(dt), 
                                Weather(temp, feels_like, weather))
                            )

                        return WeatherForecast(forecast)

                    except KeyError:
                        return None
        return None
    
    
    async def get_weather_forecast(self, city_name: str) -> WeatherForecast | None:
        coords = await self.get_city_location(city_name)
        if not coords:
            return None
        
        (lat, lon) = coords

        return await self.get_weather_forecast_coords(lat, lon)
    
    async def get_weather(self, city_name: str) -> Weather | None:
        coords = await self.get_city_location(city_name)
        if not coords:
            return None
        
        (lat, lon) = coords

        return await self.get_weather_coords(lat, lon)
