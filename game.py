def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are two paths ahead.")
    first_choice()

def first_choice():
    choice = input("Do you want to go left or right? (left/right): ").lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        first_choice()

def left_path():
    print("You walk down the left path and encounter a wild animal!")
    choice = input("Do you want to (run) away or (fight) the animal? ").lower()
    
    if choice == "run":
        print("You successfully escape and find a way out of the forest. You win!")
    elif choice == "fight":
        print("The animal is too strong! You have been defeated. Game over.")
    else:
        print("Invalid choice. Please choose 'run' or 'fight'.")
        left_path()

def right_path():
    print("You walk down the right path and find a treasure chest!")
    choice = input("Do you want to (open) the chest or (leave) it alone? ").lower()
    
    if choice == "open":
        print("You found gold and jewels! You win!")
    elif choice == "leave":
        print("You walk away safely, but you missed out on the treasure. Game over.")
    else:
        print("Invalid choice. Please choose 'open' or 'leave'.")
        right_path()

# Start the game
if __name__ == "__main__":
    start_game()