"""
10. Recursive Function
Problem: Create a recursive function to calculate the factorial of a number.
"""
factorial_number=int(input("Enter the factorial number "))
def find_factorial(factorial_number):
    if(factorial_number==1 or factorial_number==0):
        return 1
    else:
        return factorial_number*find_factorial(factorial_number-1)

result=find_factorial(factorial_number)
print(f"The factorial of {factorial_number} is {result}")
