import random

def get_roll():
    """Randomly select a roll number"""
    return random.randint(49,96)


def main():
    print("Welcome to the test!")
    input("Press Enter to generate roll number ...\n")

    #Display the number
    print("\nGenerated Roll: ")
    print(get_roll())

if __name__=="__main__":
    main()
