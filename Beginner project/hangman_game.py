import random

# Word list
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word
chosen_word = random.choice(word_list)

# Create placeholder
display = ""
for i in range(0, 0 + 1):  # just initializing once
    for letter in chosen_word:
        display += "_"

# Number of chances (lives)
lives = 6

# Game loop
game_over = False
while not game_over:
    print("\n" + display)
    guess = input("Guess a letter: ").lower()

    # Update display if guess is correct
    new_display = ""
    correct_guess = False

    for index in range(len(chosen_word)):
        if display[index] != "_":
            new_display += display[index]
        elif chosen_word[index] == guess:
            new_display += guess
            correct_guess = True
        else:
            new_display += "_"

    if not correct_guess:
        lives -= 1
        print("Wrong guess. Lives left:", lives)

    display = new_display

    # Check if the player won
    if "_" not in display:
        print("\n" + display)
        print("You won! 🎉")
        game_over = True

    # Check if the player lost
    if lives == 0:
        print("You lost! The word was:", chosen_word)
        game_over = True
