import random

choice = ["Rock", "Paper", "Scissors"]

game = True
while game:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
        break
        game = False
    else:
        print(f"You chose {choice[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose {choice[computer_choice]}")

    for i in range(3):
        if  user_choice == 0 and (computer_choice == 1 or computer_choice == 2):
            print("You win")
            break
        elif user_choice == 1 and (computer_choice == 0 or computer_choice == 2):
            print("You lose")
            break
        elif user_choice == 2 and computer_choice == 0:
            print("You lose!")
            break
        elif user_choice == 2 and computer_choice == 1:
            print("You win!")
            break
        else:
            print("It's a draw")
            break

    continue_game = input("Do you want to play again? Type 'y' or 'n'.\n")

    if continue_game == "n":
        game = False




