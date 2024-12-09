"""
8.  Prime Number Checker
Problem: Check if a number is prime.
    """
import math

while(1):
    num=int(input("Enter number "))

    def is_prime(number):
        if(number<0 or number==1):
            print(f"{number} is not  prime number")
            return False
        if(number%2==0):
            print(f"{number} is not prime number")
            return False
        for i in range(3, int(math.sqrt(number)+1), 2):
            if number%i==0:
                print(f"{num} is not  prime number")
                return False
        print(f"{num} is prime number")
        return True
            
	
    if not is_prime(num):
        exit()


