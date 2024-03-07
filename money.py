from menu import MENU


class Money:
    def __init__(self):
        self.change = None

    def checking(self, beverage):
        print("Please insert coins.")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        total_in_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        self.change = round(total_in_money - float(MENU[beverage]["cost"]), 2)
        if self.change < 0:  # which means the money entered is less than the cost of the beverage.
            print("Not enough money, money refunded.")
            return False
        else:
            return True
