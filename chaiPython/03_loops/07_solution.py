"""
7.  Validate Input
Problem: Keep asking the user for input until they enter a number
between 1 and 10.
    """
while(1):
    number=int(input("Enter the number "))
    if(number>=1 and number<=10):
        exit()

