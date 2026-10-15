import random

# ASCII Art for the Hangman stages (0 to 6 wrong guesses)
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |

     |   |
         |
        ===""",
    """
    +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\  |
    / \  |
        ===""",
]

# Word bank for the game
WORDS = [
    "python",
    "developer",
    "programming",
    "hangman",
    "computer",
    "algorithm",
    "jupyter",
    "variable",
]


def play_hangman():
    # Setup initial game state
    secret_word = random.choice(WORDS).lower()
    guessed_letters = set()
    wrong_guesses = 0
    max_turns = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")

    while wrong_guesses < max_turns:
        print(HANGMAN_PICS[wrong_guesses])

        # Display the hidden word progress (e.g., p _ t h _ n)
        word_display = [
            char if char in guessed_letters else "_" for char in secret_word
        ]
        print("Word: " + " ".join(word_display))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        # Check for victory condition
        if "_" not in word_display:
            print(f"\n🎉 Congratulations! You guessed the word: {secret_word}")
            break

        # Process user input
        guess = input("\nGuess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single alphabetical letter.")
            continue
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            continue

        # Log the guess
        guessed_letters.add(guess)

        # Check if guess is right or wrong
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Sorry, '{guess}' is not in the word.")
            wrong_guesses += 1
    else:
        # Executes only if the loop runs out without hitting the break statement
        print(HANGMAN_PICS[wrong_guesses])
        print(f"\n💀 Game Over! You ran out of tries. The word was: {secret_word}")


if __name__ == "__main__":
    play_hangman()
