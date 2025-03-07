print("Welcome to the Number Guessing Game!")

import random
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5
def guess_number():
    global attempts
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
    elif guess > number:
        print("Too high.")
        attempts -= 1
        if attempts > 0:
            guess_number()
        else:
            print("You've run out of guesses, you lose.")
    else:
        print("Too low.")
        attempts -= 1
        if attempts > 0:
            guess_number()
        else:
            print("You've run out of guesses, you lose.")
            
guess_number()
