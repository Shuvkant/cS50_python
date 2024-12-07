"""
8.  Password Strength Checker
Problem: Check if a password is “Weak”, “Medium”, or “Strong”. Criteria:
< 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
    """

password=str(input("Enter the password "))
password_length=len(password)

if(password_length<6):
    print("Password is weak ", password)
elif(password_length>=6 and password_length<=10):
    print("Password is medium ", password)
elif(password_length>10):
    print("Password is strong", password )
else:
    print("Invalid password", password)
