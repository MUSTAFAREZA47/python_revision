print("Mathematical Python Calculator")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

for operation in ["+", "-", "*", "/"]:
    print(f"\n{operation}")

operation = input("Pick an operation: ")

def calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number
    else:
        return "Invalid operation"


result = calculate(first_number, second_number, operation)
print(f"{first_number} {operation} {second_number} = {result:.2f}")