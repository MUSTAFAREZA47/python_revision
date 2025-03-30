print("Welcome to Higher Lower Game!")

import random
from data import data

score = 0

def get_random_account():
    random_account = random.choice(data)
    return random_account

def format_account(account):
    """Format the account into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(user_guess, a_followers, b_followers):
    """Check if the user's guess is correct."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
game_should_continue = True

account_b = get_random_account()

while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    if account_a == account_b:
        account_b = get_random_account()


    print(f"Compare A: {format_account(account_a)}")
    print("\nVS\n")
    print(f"Against B: {format_account(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]


        
    is_correct = check_answer(guess, a_followers, b_followers)


    if is_correct:
        score += 1
        print(f"\nYou are correct! Current score: {score}")
    else:
        print(f"\nSorry, that's wrong. Final score: {score}")
        print("Game over.")
        game_should_continue = False