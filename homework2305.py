from abc import ABC, abstractmethod
from typing import Self


class Transport(ABC):
    def __init__(self, fuel: int, condition: int):
        self.__fuel = fuel
        self.__condition = condition

    @property
    def fuel(self) -> int:
        return self.__fuel

    @property
    def condition(self) -> int:
        return self.__condition

    @property
    def is_working(self) -> bool:
        return self.__condition > 30

    @abstractmethod
    def __str__(self) -> str:
        return ''

    def move(self, distance: int):
        if not self.is_working:
            print('Transport is broken')
            return

        fuel_needed = distance // 2

        if self.__fuel < fuel_needed:
            print('Not enough fuel')
            return

        self.__fuel -= fuel_needed
        self.__condition -= distance // 5

        if self.__condition < 0:
            self.__condition = 0

        print(f'Transport moved {distance} km')

    def repair_condition(self, value: int):
        self.__condition += value

        if self.__condition > 100:
            self.__condition = 100


class Car(Transport):
    def __init__(self, model: str):
        super().__init__(fuel=50, condition=100)
        self.model = model

    def __str__(self) -> str:
        return f'Car {self.model} fuel={self.fuel} condition={self.condition}'


class Truck(Transport):
    def __init__(self, name: str):
        super().__init__(fuel=120, condition=100)
        self.name = name

    def __str__(self) -> str:
        return f'Truck {self.name} fuel={self.fuel} condition={self.condition}'


class Motorcycle(Transport):
    def __init__(self, brand: str):
        super().__init__(fuel=20, condition=100)
        self.brand = brand

    def __str__(self) -> str:
        return f'Motorcycle {self.brand} fuel={self.fuel} condition={self.condition}'


class ServiceStation:
    def repair(self, transport_unit: Transport):
        transport_unit.repair_condition(40)
        print('Transport repaired')


car = Car('BMW')
truck = Truck('MAN')
motorcycle = Motorcycle('Yamaha')

print(car)
print(truck)
print(motorcycle)

print(car.is_working)
print(car.__dict__)

car.move(20)
print(car)

car.move(1000)

motorcycle.move(50)
print(motorcycle.is_working)

motorcycle.move(10)

service = ServiceStation()

service.repair(motorcycle)
print(motorcycle)

service.repair(motorcycle)
print(motorcycle)

broken_car = Car('Audi')

broken_car.move(300)
print(broken_car)

print(broken_car.is_working)

service.repair(broken_car)
print(broken_car)

service.repair(broken_car)
print(broken_car)