"""
3.  Multiplication Table Printer
Problem: Print the multiplication table for a given number up to 10, but
skip the fifth iteration.
    """
desired_number=int(input("Enter the required number "))
for x in range(10):
    if(x+1==5):
        continue
    print(f"{desired_number}*{x+1}={(x+1)*desired_number}")
