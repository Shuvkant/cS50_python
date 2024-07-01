#defining functions
def hello(to):
    print('Hello,', to)

# Ask user to enter their name
def main():
    name=input("Enter your name ").strip().title()
    hello(name)

main()
