import random

print("Welcome to Password Generator!")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"

user_letters = input("How many letters would you like in your password?\n")
user_numbers = input("How many numbers would you like?\n")
user_symbols = input("How many symbols would you like?\n")

def password_generator():
    password = ""
    for letter in range(int(user_letters)):
        password += random.choice(alphabet)
    for number in range(int(user_numbers)):
        password += random.choice(numbers)
    for symbol in range(int(user_symbols)):
        password += random.choice(symbols)
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    print(f"Your password is: {password}")

password_generator()

