print("Welcome to the tip calulator.") 

total_bill = float(input("What was the total bill? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
spliting_bill = int(input("How many people to split the bill? " ))
amount_per_person = (total_bill + (total_bill * tip_amount / 100)) / spliting_bill

print(f"Each person should pay: ${amount_per_person:.2f}")

# height = 1.65 
# weight = 84

# # Write your code here.
# # Calculate the bmi using weight and height.
# bmi = round(float(weight / (height**2)))

# print(bmi)
