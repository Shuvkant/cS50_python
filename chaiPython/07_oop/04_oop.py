"""
Problem: Modify the Car class to encapsulate the brand attribute, making it private, and
provide a getter method for it.
    """


class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def printname(self):
        print(self.get_brand(), self.model)


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Use parent class initializer
        self.battery_size = battery_size

    def printelectric(self):
        print(self.get_brand(), self.model, self.battery_size)


x = ElectricCar(brand="suzuki", model="490", battery_size="70")
x.printelectric()
