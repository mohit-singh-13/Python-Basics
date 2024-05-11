class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def fullName(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are amazing"
    
    @property
    def model(self):
        return self.__model
    
my_car = Car("Tata", "Safari")

# my_car.__model = "City"
# print(my_car.__model)

print(my_car.model)

# print(my_car.model())


print(isinstance(my_car, Car))