# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# screen = Screen()
# print(screen.canvheight)
# screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
#
# table.field_names = ["Poke Name", "Type"]
# table.add_rows([
#     ["Pikachu", "Electric"],
#     ["Squirtle", "Water"],
#     ["Charmander", "Fire"]
# ])
#
# table.align = "c"
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_machine_on = True
while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        print("Coffee Machine is getting off")
        is_machine_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):

                coffee_maker.make_coffee(drink)





