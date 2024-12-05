""" 
1.  Age Group Categorization

Classify a person’s age group: Child (< 13), Teenager (13-19), Adult
(20-59), Senior (60+).
    """
choice=True
while(choice):
    age=int(input("\nEnter your age "))
    if (age<13):
        print("Child")
    elif(age>=13 and age<=19):
        print("Teenager")
    elif(age>=20 and age<=59):
        print("Adult")
    else:
        print("Senior citizen")

    choice=str(input("Do you want to exit (y/n)"))
    if (choice=='y'):
        choice=False
print("Program executed successfully")

