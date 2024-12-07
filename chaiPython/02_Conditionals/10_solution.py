"""
10. Pet Food Recommendation
Problem: Recommend a type of pet food based on the pet’s species and
age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat
food).
"""
pets=["Cat" , "Dog"]
print(*pets)
pet=str(input("Enter the pet "))
age=int(input("Enter the age of the pet "))
if(pet=="dog"):
    if(age<2):
        food="Puppy food"
    else:
        food="adult puppy food"
else:
    if(age>5):
        food="senior cat food"
    else:
        food="junior  cat food"


print(f"{pet} should have {food}")
