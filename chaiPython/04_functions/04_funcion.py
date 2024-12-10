"""
4. Function Returning Multiple Values
Problem: Create a function that returns both the area and circumference of
a circle given its radius.
    """
import math
radius=float(input("Enter the radius of the circle "))
def area_circumference(rad):
    circumference=2*math.pi*rad
    area=math.pi*(rad**2)
    return circumference, area

circumference, area=area_circumference(radius)
print(f"The circumference is {circumference:.2f}")
print(f"The area  is {area :.2f}")


