"""
2.  Sum of Even Numbers
Problem: Calculate the sum of even numbers up to a given number n.
    """
number=int(input("Enter the number to find sum upto "))
print(f"The number is {number}")
if(number%2==0):
    number=number
    print(f"You entered even number: {number}")
else:
    number=number-1
    print(f"You entered odd number: {number+1}")

upto=int(number/2);
sum=0
number=2
for x in range(upto):
    sum=sum+number
    number+=2

print(f"The sum is {sum}")
