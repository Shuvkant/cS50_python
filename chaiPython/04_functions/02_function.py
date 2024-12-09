"""
2. Function with Multiple Parameters
Problem: Create a function that takes two numbers as parameters and returns their sum.
    """
num_one=float(input("Enter first number "))
num_two=float(input("Enter second number "))

def sum_of_numbers(a,b):
    return a+b

result=sum_of_numbers(num_one, num_two)
print(f"The sum of {num_one} and {num_two} is {result}")
