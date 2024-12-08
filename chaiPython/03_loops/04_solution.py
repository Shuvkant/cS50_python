"""
4.  Reverse a String
Problem: Reverse a string using a loop.
    """

input_string=str(input("Enter the string "))
input_string_length=len(input_string)
print(input_string_length)
y=0
reverse_string=""
for x in input_string:
    reverse_string=reverse_string+input_string[input_string_length-(y+1)]
    y+=1
print(f"The original string was {input_string}")
print(f"The reversed string is {reverse_string}")
