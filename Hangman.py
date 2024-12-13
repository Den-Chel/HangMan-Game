import random


def hangman():
    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    # List of words to choose 
    word_list = ["python", "developer", "hangman", "challenge", "portfolio"]
    secret_word = random.choice(word_list).lower()
    guessed_letters = set()
    attempts = 6  

    # Generate the word
    word_display = ["_"] * len(secret_word)

    while attempts > 0 and "_" in word_display:
        print("\n" + " ".join(word_display))
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        print(f"Remaining Attempts: {attempts}")

        guess = input("Guess a letter: ").lower()

        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            # Reveal guessed letters in the word display
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    word_display[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

    # Check if the player won or lost
    if "_" not in word_display:
        print("\nCongratulations! You guessed the word:", secret_word)
    else:
        print("\nGame over! The word was:", secret_word)


# Run the game
if __name__ == "__main__":
    hangman()
