from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu = Menu()
# menuItem = menu.find_drink("espresso")
# print(menuItem.name)

is_on = True
while is_on:
    enteredChoice = input("What would you like? (espresso/latte/cappuccino):")
    coffeeMaker = CoffeeMaker()
    moneyMachine = MoneyMachine()

    if (enteredChoice == "off"):
        is_on = False
    elif (enteredChoice == "report"):
        coffeeMaker.report()
    else:
        menu = Menu()

        # drink_selected is a menuItem object
        drink_selected = menu.find_drink(enteredChoice)
        # print(drink_selected.ingredients)
        is_res_sufficient = coffeeMaker.is_resource_sufficient(drink_selected)
        if (is_res_sufficient):
            cost_of_drink = drink_selected.cost
            is_money_enough = moneyMachine.make_payment(cost_of_drink)
            if(is_money_enough):
                coffeeMaker.make_coffee(drink_selected)
                is_on = False

            else:
                print("Goodbye!")
                is_on = False
        
        
        