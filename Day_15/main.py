from data import Menu
from data import Resource

# check coffee machine is off or on
machine_status = input("Do you want to turn the coffee machine on or off? (on/off): ").lower()
status = machine_status

# Check if the coffee machine is on or off
def check_machine_status(status):
    if status == "off":
        print("The coffee machine is off.")
        return False
    elif status == "on":
        print("\nThe coffee machine is on.")
        return True
    else:
        print("Invalid status. Please enter 'on' or 'off'.")
        return False

# check if there are enough resources
def is_enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= Resource[item]:
            print("Sorry, there is not enough {}.".format(item))
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change_money = round(money_received - drink_cost)
        print(f"Here is your ${change_money} change")
        Resource['profit'] += drink_cost
        return True
    else:
        print("Sorry, That's not enough money, Money Refunded!")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        Resource[item] -= order_ingredients[item]
    print(f"Here is your ${drink_name} ready ☕️. Enjoy Well!")


def process_coin():
    """ Return total after processing the total money"""
    print("Please, Insert the coin.")
    total = int(input("how many quaters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
    
while check_machine_status(status):
    # Ask user for input
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "report":
        print("Water: {}ml".format(Resource["water"]))
        print("Milk: {}ml".format(Resource["milk"]))
        print("Coffee: {}g".format(Resource["coffee"]))
        print("Profit: ${}".format(Resource["profit"]))
    elif choice == "off":
        print("Turning off the coffee machine.")
        status = "off"
        break
    else: 
        drink = Menu[choice]
        print(drink)
        
        # Check if there are enough resources
        if is_enough_resources(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
               make_coffee(choice, drink["ingredients"])


        
        

    