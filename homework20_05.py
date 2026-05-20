class Car:
    def __init__(self, model: str, age: int, owner: str = "", fuel: float = 0) -> None:
        self.model = model.strip().title()
        self.age = age
        self.owner = owner
        self.fuel = fuel
        self.car_id = id(self)

    def __str__(self) -> str:
        return f'<{self.model}: {self.car_id}. Fuel: {self.fuel}L>'

    def add_fuel(self, amount: float):
        self.fuel += amount

    @property
    def car_condition(self) -> str:
        if self.age <= 3:
            return "нове авто"
        elif self.age <= 10:
            return "середній стан"
        else:
            return "старе авто"

    @property
    def fuel_status(self) -> str:
        if self.fuel < 10:
            return "Потрібно заправитись"
        elif self.fuel < 40:
            return "Достатньо бензину"
        else:
            return "Можна їхати далеко"


car_1 = Car(model='   bmw m5', age=2)
print(id(car_1))

print(car_1.__dict__)
print(car_1)

car_1.fuel += 20
print(car_1)

car_1.add_fuel(35)
print(car_1)

condition_1 = car_1.car_condition
print(condition_1)

fuel_status_1 = car_1.fuel_status
print(fuel_status_1)

car_2 = Car(model='audi a6', age=12, owner='Alex', fuel=15)

print(car_1.__dict__)
print(car_2.__dict__)

print(car_2)

condition_2 = car_2.car_condition
print(condition_2)

fuel_status_2 = car_2.fuel_status
print(fuel_status_2)

if car_1.fuel > car_2.fuel:
    print(f'У {car_1.model} більше бензину')
elif car_1.fuel < car_2.fuel:
    print(f'У {car_2.model} більше бензину')
else:
    print('Кількість бензину однакова')