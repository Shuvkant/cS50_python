"""
6.  Factorial Calculator
Problem: Compute the factorial of a number using a while loop.
"""
number=int(input("Enter the number: "))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def another_factorial(n):
    result=1 
    while(n>1):
        result=result*n 
        n-=1
    return result
fact=another_factorial(number)

print(f"Factorial of {number} is {fact} ")
