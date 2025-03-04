print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if left_or_right == "left":
    swim_or_wait = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if swim_or_wait == "swim":
        door_color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
        if door_color == "yellow":
            print("You found the treasure! You Win!")
        elif door_color == "red":
            print("It's a room full of fire. Game Over.")
        elif door_color == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")