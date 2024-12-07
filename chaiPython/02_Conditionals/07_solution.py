"""
7.  Coffee Customization
Problem: Customize a coffee order: “Small”, “Medium”, or “Large” with an
option for “Extra shot” of espresso.
    """
coffee=["Small", "Medium", "Large"]
print(*coffee)
select_coffee=str(input("Enter the coffee "))
shot=input("Do you want extra shot of espresso? (y/n)")
if(shot=="y"):
    shot="Extra shot"
    print("You have ordered ", select_coffee +" coffee with " , shot)
else:
    shot=""
    print("You have ordered ", select_coffee +" coffee")

