# Task 1: Hangman Game
import random

words = ["python", "program", "keyboard", "internet", "computer"]
word = random.choice(words)

guessed = []        # letters the player has guessed
wrong = 0           # number of wrong guesses
max_wrong = 6

print("=== HANGMAN ===")

while wrong < max_wrong:
    # show the word with blanks
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)

    # check if player has won
    if "_" not in display:
        print("You won! The word was", word)
        break

    print("Wrong guesses left:", max_wrong - wrong)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
    elif guess in guessed:
        print("You already guessed that.")
    else:
        guessed.append(guess)
        if guess in word:
            print("Correct!")
        else:
            wrong += 1
            print("Wrong!")
else:
    print("\nGame over! The word was", word)
