# import random

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "scissors" and computer_choice == "paper") or \
#          (user_choice == "paper" and computer_choice == "rock"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# # Main game function
# def play_game():
#     # List of possible choices
#     choices = ["rock", "paper", "scissors"]
    
#     # Get user input
#     user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
#     # Validate input
#     if user_choice not in choices:
#         print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
#         return
    
#     # Computer randomly chooses
#     computer_choice = random.choice(choices)
    
#     # Show choices
#     print(f"You chose: {user_choice}")
#     print(f"Computer chose: {computer_choice}")
    
#     # Determine winner
#     result = determine_winner(user_choice, computer_choice)
#     print(result)

# # Play the game
# if __name__ == "__main__":
#     play_game()

import random

# taking user input
while True:
    print("--->Welcome In The World Of RPS Game<---")
    rps_start = input("You want to start the game. (y/n): ")
    if rps_start.lower != "y":
        break
    print("Enter 'Q' to quit\n")
    
    userinput = input("Enter the choice(rock,paper,scissors):")

    # generating computer selection
    options = ["rock","paper","scissors"]
    comp_choice = random.choice(options)
    print(comp_choice)

    print(f"\nYou chose{userinput}, computer chos{comp_choice}.\n")

    def rps_game(user_choice, computer_choice):
        if userinput == comp_choice:
                return "It's a tie!"
        elif (userinput == "rock" and comp_choice == "scissors") or \
                (userinput == "scissors" and comp_choice == "paper") or \
                (userinput == "paper" and comp_choice == "rock"):
                return "You win!"
        else:
            return "Computer wins!"
    
