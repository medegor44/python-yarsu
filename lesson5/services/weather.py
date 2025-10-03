class Weather:
    _temp: float
    _weather: str
    _temp_feels_like: float

    def __init__(self, temp: float, weather: str, temp_feels_like: float) -> None:
        self._temp = temp
        self._weather = weather
        self._temp_feels_like = temp_feels_like

    @property
    def temp(self) -> float:
        return self._temp

    @property
    def weather(self) -> str:
        return self._weather

    @property
    def temp_feels_like(self) -> float:
        return self._temp_feels_like