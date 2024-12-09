"""
5. Default Parameter Value
Problem: Write a function that greets a user. If no name is provided,
it should greet with a default name.
    """
def greet_user(name="bunny"):
    print(f"Hello {name}")

greet_user('Ram')
greet_user('Michael')
greet_user()
