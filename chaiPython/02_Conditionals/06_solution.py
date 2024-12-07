"""
6.  Transportation Mode Selection
Problem: Choose a mode of transportation based on the distance (e.g., <3
km: Walk, 3-15 km: Bike, >15 km: Car).
    """

distance=int(input("Enter the distance to be covered "))
if(distance<3):
    mode="walk"
elif(distance>=3 and distance<=15):
    mode="bike"
elif(distance>15):
    mode="car"
print("The mode of transportation suggested by AI is ", mode)
