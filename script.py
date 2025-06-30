import random  # Module for generating random numbers (e.g., for computer's choice)
import ascii  # Assuming this module contains your ASCII art strings (rcok, paper, scissors)

# Prompt the user for their choice and convert it to lowercase
# This ensures consistent comparison later, regardless of user input casing (e.g., "Rock", "ROCK", "rock")
user_choice = input("Rock, Paper or Scissors?\n").lower()

# Define a list of the choice names in lowercase for consistent comparison
# This list is used for both displaying the user's choice and for comparison logic
items = ["rock", "paper", "scissors"]

# Define a list of ASCII art corresponding to each choice, in the same order as 'items'
ascii_art = [ascii.rcok, ascii.paper, ascii.scissors]

# --- Handle User's Choice: Display ASCII Art and Confirm Choice ---
# This block checks the user's input and prints the corresponding ASCII art and choice name.
# It also implicitly determines if the user provided a valid input.
if user_choice == "rock":
    print(ascii_art[0], items[0])  # Prints ASCII art for rock and the string "rock"
elif user_choice == "aper":  # !! IMPORTANT: This is a typo. Should be "paper" !!
    print(ascii_art[1], items[1])  # Prints ASCII art for paper and the string "paper"
elif user_choice == "scissors":
    print(
        ascii_art[2], items[2]
    )  # Prints ASCII art for scissors and the string "scissors"
# Consider adding an 'else' block here to handle invalid user input,
# perhaps printing an error and exiting the program to prevent further issues.
else:
    print("Invalid choice! Please enter 'Rock', 'Paper', or 'Scissors'.")
    # For a simple game, you might exit here:
    # exit()


# --- Generate Computer's Choice ---
# Generate a random integer between 0 and 2 (inclusive) to select an item from the 'items' list.
pc_choice_random_number = random.randint(0, 2)
# Retrieve the computer's choice name (e.g., "rock", "paper", "scissors") based on the random number.
pc_choice = items[pc_choice_random_number]
# Print the computer's ASCII art and its chosen name.
print(ascii_art[pc_choice_random_number], pc_choice)


# --- Determine the Winner ---
# This section contains the core game logic to decide if it's a tie, a win, or a loss.

# Check for a tie condition: if both user and computer chose the same item.
# This comparison is now correctly case-insensitive because both 'user_choice' and 'pc_choice'
# are in lowercase (due to '.lower()' on user input and 'items' list being lowercase).
if user_choice == pc_choice:
    print("It's a tie")
# Check for all winning conditions for the user using logical OR.
# Each inner condition checks for a specific user_choice vs. pc_choice pair that results in a win.
elif (
    (user_choice == "rock" and pc_choice == "scissors")  # Rock beats Scissors
    or (user_choice == "paper" and pc_choice == "rock")  # Paper beats Rock
    or (user_choice == "scissors" and pc_choice == "paper")  # Scissors beats Paper
):
    print("You Win!!")
# If it's not a tie and not a win for the user, then it must be a loss.
else:
    print("You Lose!")
