import random

def print_hangman(stage):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    print(stages[stage])

def hangman():
    print("Welcome to Hangman!")
    
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    
    display = ["_"] * word_length
    correct_guesses = []
    incorrect_guesses = []
    max_attempts = 6
    attempts = 0
    
    print_hangman(attempts)
    print(" ".join(display))
    
    while attempts < max_attempts:
        guess_letter = input("\nGuess a letter: ").lower()
        
        if guess_letter in correct_guesses or guess_letter in incorrect_guesses:
            print(f"You've already guessed '{guess_letter}'. Try a different letter.")
            continue
        
        if guess_letter in chosen_word:
            print(f"Good job! '{guess_letter}' is in the word.")
            correct_guesses.append(guess_letter)
            for index, letter in enumerate(chosen_word):
                if letter == guess_letter:
                    display[index] = letter
        else:
            print(f"Sorry, '{guess_letter}' is not in the word.")
            incorrect_guesses.append(guess_letter)
            attempts += 1
        
        print_hangman(attempts)
        print(" ".join(display))
        print(f"Correct guesses: {', '.join(correct_guesses)}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Remaining attempts: {max_attempts - attempts}")
        
        if "_" not in display:
            print("Congratulations! You've guessed the word correctly!")
            break
    
    if attempts == max_attempts:
        print(f"Game over! The word was '{chosen_word}'.")

if __name__ == "__main__":
    hangman()