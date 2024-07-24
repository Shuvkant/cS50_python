import re

email=input("Enter your email ").strip()

# for something left of the @ and something right of the @
if re.search(r"^\w+@(\w+\.)?\w+\.(edu)$", email, re.IGNORECASE):
    print("valid")
else:
    print("Invalid")

