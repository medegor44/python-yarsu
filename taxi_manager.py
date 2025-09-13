import math

DRIVE_STATUS_FREE = "free"
DRIVE_STATUS_IN_DRIVE = "in_drive"
DRIVE_STATUS_FINISHED = "finished"



class Position:
    __x: float
    __y: float

    def __init__(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def subtract(self, position: Position):
        return Position(self.x - position.x, self.y - position.y)

    def len(self):
        return math.sqrt(self.x**2 + self.y**2)

class Client:
    __position: Position
    @property
    def position(self):
        return self.__position

class Car:
    __position: Position
    __is_available: bool
    __client: Client

    @property
    def position(self):
        return self.__position
    
    @property
    def is_available(self):
        return self.__is_available
    
    @is_available.setter
    def is_available(self, value: bool):
        self.__is_available = value

    @property
    def client(self):
        return self.__client
    
    @client.setter
    def client(self, value: Client):
        self.__client = value

class Drive:
    __car: Car
    __client: Client
    __status: str

    def __init__(self, car: Car, client: Client) -> None:
        self.__car = car
        self.__status = DRIVE_STATUS_IN_DRIVE
        self.__client = client


class TaxiManager:
    __cars: list[Car]

    def get_available_cars(self) -> list[Car]: 
        return [car for car in self.__cars if car.is_available]

    def get_taxi(self, client: Client):
        nearestCar = None

        for car in self.get_available_cars():
            if (nearestCar == None or 
                client.position.subtract(nearestCar.position()).len() > 
                client.position.subtract(car.position())):
                nearestCar = car
        
        nearestCar.is_available = False
        nearestCar.client = client

        return nearestCar

