MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# check if res sufficient
def is_resource_sufficient(order_ingredients):
    """Returns true when orders can be made, false when ingredients are insufficient"""
    is_sufficient = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            is_sufficient = False
            print(f"Sorry there is not enough {item}")

    return is_sufficient


def process_coins():
    """Returns the total calculated from Coins inserted"""
    print("Please insert coins.")
    total = int(input("Number of quarters: ")) * 0.25
    total += int(input("Number of dimes: ")) * 0.10
    total += int(input("Number of nickels: ")) * 0.05
    total += int(input("Number of pennies: ")) * 0.01

    return total


def check_transaction(amount_paid, cost_of_drink):
    """ Return true when payment accepted, return false if money insufficient"""
    is_sufficient = True
    if amount_paid <= cost_of_drink:
        is_sufficient = False

        print("Sorry that's not enough money. Money refunded.")
        print(f"Here is your change: {amount_paid}")
    else:
        change = round(amount_paid - cost_of_drink, 2)
        print(f"Here is your change: {change}")
        global money_profit
        money_profit += costOfDrink

    return is_sufficient


def make_coffee(drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")



# check if machine is on
is_on = True
money_profit = 0
# keep asking
while is_on:
    # print(MENU["espresso"]["cost"])
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {money_profit}")
    else:
        drink = MENU[choice]
        costOfDrink = MENU[choice]["cost"]
        # check if ingredients sufficient
        if is_resource_sufficient(drink["ingredients"]):
            print(f"The {choice} costs ${MENU[choice]['cost']}")

            amountInserted = process_coins()
            print(f"You have inserted {amountInserted}")

            if check_transaction(amountInserted, costOfDrink):
                make_coffee(choice, drink["ingredients"])

# def print_hi(name):
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#
