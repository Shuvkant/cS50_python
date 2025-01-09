"""
3. Inheritance
Problem: Create an ElectricCar class that inherits from the Car class and has an additional
attribute battery_size.
"""


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def printname(self):
        print(self.brand, self.model)


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.brand = brand
        self.model = model
        self.battery_size = battery_size

    def printelectric(self):
        print(self.brand, self.model, self.battery_size)


x = ElectricCar(brand="rabxf", model="gsfgs", battery_size="50")
x.printelectric()
