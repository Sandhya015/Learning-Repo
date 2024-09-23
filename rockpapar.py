import random

def play_game():
    print("Choose an option: \n0 for Rock\n1 for Paper\n2 for Scissors")
    
    # Getting the user's input (0 for Rock, 1 for Paper, 2 for Scissors)
    user_choice = int(input("Enter 0, 1, or 2: "))
    
    # Validate the input
    if user_choice not in [0, 1, 2]:
        print("Invalid input! Please try again.")
        return
    
    # Map the user's input to rock, paper, or scissors
    choices = ['rock', 'paper', 'scissors']
    user_choice_name = choices[user_choice]
    
    # Random choice for the computer
    computer_choice = random.randint(0, 2)
    computer_choice_name = choices[computer_choice]
    
    # Display choices
    print(f"\nYou chose {user_choice_name}.")
    print(f"The computer chose {computer_choice_name}.\n")

    # Determine the winner using if-else
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")

# Play the game
if __name__ == "__main__":
    play_game()
