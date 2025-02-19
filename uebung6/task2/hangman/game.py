from typing import Set


def _create_display_word(word: str, guessed_letters: Set[str]) -> str:
    """
    Creates a display string showing the current state of the word.

    Args:
        word (str): The word to be guessed
        guessed_letters (Set[str]): A set of all letters guessed so far

    Returns:
        str: The displayed string with unguessed letters shown as '_'
    """
    return "".join(letter if letter in guessed_letters else '_' for letter in word)


def _get_valid_guess() -> str:
    """
    Prompts the user for a single letter input and validates it.

    Returns:
        str: A single valid letter
    """
    while True:
        guess: str = input("Rate einen Buchstaben: ").strip().lower()

        # Return single valid letter
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Bitte gib einen Buchstaben ein!")


def start(word: str, max_attempts: int = 6) -> bool:
    """
    Main game loop for Hangman.

    Args:
        word (str): The word to be guessed
        max_attempts (int): Maximum number of incorrect guesses allowed (default: 6)

    Returns:
        bool: True if the word is guessed correctly, False otherwise
    """

    # Initialize game variables
    guessed_letters: Set[str] = set()
    wrong_guesses: int = 0

    # Game introduction message
    print("\nWillkommen beim Hangman-Spiel!")
    print(f"Du hast {max_attempts} Fehlversuche.")

    # Main game loop
    while wrong_guesses < max_attempts:
        # Create current display of the word
        display_word: str = _create_display_word(word, guessed_letters)

        # Check if the word has been guessed
        if display_word == word:
            print(f"\nGratulation! Das Wort war {display_word}.\nDu hast {wrong_guesses} Fehlversuche benötigt.")
            return True

        # Show current game state
        print(f"\nAktuelles Wort: {display_word}\nFehlversuche: {wrong_guesses}/{max_attempts}")

        # Get letter guess
        guess: str = _get_valid_guess()

        # Check if letter has already been guessed
        if guess in guessed_letters:
            print("Diesen Buchstaben hast du bereits geraten!")
            continue

        # Add guessed letter to the set
        guessed_letters.add(guess)

        # Check if the letter is in the word
        if guess not in word:
            wrong_guesses += 1
            print(f"Falsch! Du hast noch {max_attempts - wrong_guesses} Versuche übrig.")

            # Check if all attempts have been used
            if wrong_guesses == max_attempts:
                print(f"\nGame Over! Das Wort war: {word}")
                return False

    return False