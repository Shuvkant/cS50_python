
import random

# List of random fortunes
fortunes = [
    "You will find great success in unexpected places.",
    "Your kindness will lead you to new friendships.",
    "A small change will bring great happiness.",
    "You will soon receive wonderful news.",
    "Your creative talents will be recognized.",
    "An exciting opportunity is waiting for you.",
    "Take a risk today—it will pay off!",
    "A challenge will lead to your personal growth.",
    "A smile can change the world around you.",
    "Trust yourself; you are capable of amazing things."
]

def get_fortune():
    """Randomly select a fortune from the list."""
    return random.choice(fortunes)

def main():
    print("Welcome to your Fortune Cookie!")
    input("Press Enter to open your fortune cookie...\n")
    
    # Display the fortune
    print("\nYour Fortune: ")
    print(get_fortune())
    
    # End with a little fortune cookie image
    print("\n--- 🍪 ---")

if __name__ == "__main__":
    main()
