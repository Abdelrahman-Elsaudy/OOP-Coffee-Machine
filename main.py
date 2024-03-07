from process import Process
from money import Money

process = Process()
money = Money()


machine_on = True
while machine_on:
    order = input("What would you like? (espresso, latte, cappuccino) or type 'report': ").lower()
    if order == "off":
        machine_on = False
    elif order == "report":
        process.report()
    else:
        if process.check_menu(order) and process.check_resources(order) and money.checking(order):
            process.brewing(order)
            print(f"Here is ${money.change} in change.")
            print(f"Here is your {order}☕, enjoy.")
