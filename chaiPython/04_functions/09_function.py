"""
9. Generator Function with yield
Problem: Write a generator function that yields even numbers up to a specified limit.
"""
number=int(input("Enter the specified limit "))
"""
start=2
while(start<=number):
    print(start)
    start=start+2
    """
def yield_function(num):
    for i in range(2, number+1, 2):
        yield i

for values in yield_function(number):
    print(values)





