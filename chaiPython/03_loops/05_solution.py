"""
5.  Find the First Non-Repeated Character
Problem: Given a string, find the first non-repeated character.
"""
input_string=str((input("Enter the string ")))
for char in input_string:
    print(char)
    if input_string.count(char)==1:
        print(f"Char is:{char}")
        break
