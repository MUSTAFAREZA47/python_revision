print("Welcome to Blackjack Game 21 🃏")

import random

cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(random.choice(cards_deck))

computer_cards.append(random.choice(cards_deck))

print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
print(f"Computer's first card: {computer_cards}, current score: {sum(computer_cards)}")

another_card = input("Type 'y' to get another card, type 'n' to pass: ")
if another_card == "y":
    user_cards.append(random.choice(cards_deck))
    computer_cards.append(random.choice(cards_deck))
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's another card: {computer_cards}, current score: {sum(computer_cards)}")
    if sum(user_cards) > 21:
        print("You went over. You lose! 😭")
    elif sum(computer_cards) > 21:
        print("Computer went over. You win! 🥳")
    elif sum(user_cards) > sum(computer_cards):
        print("You win! 🥳")
    elif sum(user_cards) < sum(computer_cards):
        print("You lose! 😭")
    else:
        print("It's a draw! 🙃")
else:
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    computer_cards.append(random.choice(cards_deck))
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    if sum(user_cards) > sum(computer_cards):
        print("You win! 🥳")
    elif sum(user_cards) < sum(computer_cards):
        print("You lose! 😭")
    else:
        print("It's a draw! 🙃")

