from random import randint

# Welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number
answer = randint(1, 100)

# Function to check the user's guess
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function to set difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10  # Easy mode: 10 attempts
    else:
        return 5   # Hard mode: 5 attempts

# Main game logic
def game():
    attempts = set_difficulty()
    guess = None

    while attempts > 0 and guess != answer:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
            check_answer(guess, answer)
            if guess != answer:
                attempts -= 1
        except ValueError:
            print("Please enter a valid number.")

    if guess != answer:
        print(f"Sorry, you've run out of attempts. The answer was {answer}.")

# Start the game
game()
