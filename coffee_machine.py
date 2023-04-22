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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

choices = ['espresso', 'latte', 'cappuccino', 'report', 'off']

def choice_drink():
    """check user input and return the dirnk of user choice"""
    user_choice = True
    while user_choice:
        drink = input(f"  What would you like? ({'/'.join(choices[:3])}): ")
        if drink not in choices:
            print(f"Please enter one of these choices ({'/'.join(choices[:3])})\n")
            continue
        else:
            user_choice = False
            return drink

def check_resources(choosen_drink):
    """check resources sufficient"""
    for k1 in MENU[choosen_drink]['ingredients']:
        for k2 in resources:
            if k2 == k1 and resources[k2] >= MENU[choosen_drink]['ingredients'][k1]:
                return True
            elif k2 == k1 and resources[k2] < MENU[choosen_drink]['ingredients'][k1]:
                print(f"Sorry there is not enough {k2}")
                return False

def process_coins():
    """process coins transaction and return total of coins"""
    num_type = True
    while num_type:
        try:
            quarter = float(input("How many quarters?: ")) * .25
            dime = float(input("How many dimes?: ")) * .10
            nickel = float(input("How many nickels?: ")) * .05
            penny = float(input("How many pennies?: ")) * .01
            total = quarter + dime + nickel + penny
            
            num_type = False
            return total
        except:
            print("please enter a number not strings\n")
            continue

money = 0
machine_on = True
while machine_on:

    drink = choice_drink()

    if drink == 'report':
        for k, v in resources.items():
            print(f"{k}: {v}")
        print(f"Money: {money}")
        continue
    elif drink == 'off':
        break

    while check_resources(choosen_drink= drink):
        total = process_coins()

        # check transaction successful.
        cost_of_dring = MENU[drink]['cost']
        if total >= cost_of_dring:
            change = round(total - cost_of_dring, 2)
            for k1 in MENU[drink]['ingredients']:
                for k2 in resources:
                    if k2 == k1 and resources[k2] >= MENU[drink]['ingredients'][k1]:
                        resources[k2] -= MENU[drink]['ingredients'][k1]
            money += cost_of_dring
            print(f"Here is ${change} in change")
            print(f"Here is your {drink} Enjoy!")
            break
        else:
            print("Sorry that's not enough money. Money refunded.")
            break
