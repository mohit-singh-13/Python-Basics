"""
class Car:
    brand = None
    model = None

my_car = Car()
print(my_car)
"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = Car("Toyota", "Corolla")

print(my_car.brand)
print(my_car.model)

print(my_car.fullName())
print()

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)
print(my_tesla.fullName())