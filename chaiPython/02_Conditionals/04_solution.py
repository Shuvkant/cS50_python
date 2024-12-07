"""
4.  Fruit Ripeness Checker

Problem: Determine if a fruit is ripe, overripe, or unripe based on its
color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
        """

fruit="Banana"
color=str(input("Enter the color of "+  fruit +" " ))
if(color=="green"):
    status="unripe"
elif(color=="yellow"):
    status="ripe"
else:
    status="overripe"

print(fruit +" is "+ status)
