"""
5. Polymorphism
Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and
ElectricCar classes, but with different behaviors.
    """


class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "Petrol"

    def printname(self):
        print(f"{self.get_brand()} of  {
              self.__model}model and fuel type is {self.fuel_type()}")

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electiricty"

    def printelectric(self):
        print(f"{self.fuel_type()} has battery_size of {self.battery_size}")


my_car = ElectricCar(brand="suzuki", model="490", battery_size="70")
# my_car.printelectric()
car = Car(brand="Yamaha", model="Cx300")
# car.printname()
# car.model = "City"
# print(Car.general_description())
print(car.model)


class battery:
    def battery_info(self):
        return "This is battery"


class engine:
    def engine_info(self):
        return "This is engine"


class electric_Car_Two(battery, engine, Car):
    pass


my_new_car = electric_Car_Two("Tesla", "s-400")
print(my_new_car.battery_info())
print(my_new_car.engine_info())
