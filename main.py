# check if input in menu.
# check if there are enough resources.
# check if money entered is enough.
# if yes, add beverage price to earnings, make beverage and give the change.

from process import Process
from money import Money

process = Process()
money = Money()
machine_on = True

while machine_on:
    beverage = input("What would you like? (espresso, latte, cappuccino) or type 'report': ").lower()
    if beverage == "off":
        machine_on = False
    elif beverage == "report":
        process.resources["money"] = money.earnings["money"]    # to merge both resources and money reports.
        process.report()
    elif process.check_menu(beverage):
        if process.check_resources(beverage) != False and money.checking(beverage) != False:
                process.brewing(beverage)
                money.collecting_money(beverage)