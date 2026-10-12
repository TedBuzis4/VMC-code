"""first input cannot handle letters or floats, accepts negatives. 
code ends if input for purchase confirm is invalid or declined, when selecting an item
item select IS case sensitive,   and will end if an invalid input is selected
 
"""
#Fixed (:

products = {
    "A1": {"name": "Water", "price": 1.00},
    "A2": {"name": "Soda", "price": 1.50},
    "A3": {"name": "Juice", "price": 1.75},
    "A4": {"name": "Chocolate Milk", "price": 1.75},
    "B1": {"name": "Chips", "price": 1.25},
    "B2": {"name": "Pretzels", "price": 1.25},
    "B3": {"name": "Popcorn", "price": 1.50},
    "B4": {"name": "Crackers", "price": 1.25},
    "C1": {"name": "Cookies", "price": 1.50},
    "C2": {"name": "Granola Bar", "price": 1.75},
    "C3": {"name": "Candy", "price": 1.00},
    "C4": {"name": "Gum", "price": 0.75},
}

def displayProducts():
    print("╔══════════════════════════════════════╗")
    print("║            VENDING MACHINE           ║")
    print("╠══════════════════════════════════════╣")

    for code, product in products.items():
        print(f"║ [{code}] {product['name']:<18} {('$' + format(product['price'], '.2f')):>12} ║")

    print("╚══════════════════════════════════════╝")

balance = 0

def displayTerminalBalance():
    print("╔═════════════╗")
    print("║   Balance:  ║")
    print("║             ║")
    print(f"║     ${balance:<7}║")
    print("║             ║")
    print("╚═════════════╝")

def startCheck():

    startInput = input("""Do you want to start the purchace? yes/no
""").lower()

    if startInput == "yes":
        displayCodeTerminal()
    elif startInput == "no":
        print("Operation Ended")
    else:
        print("""Invalid input
Type a valid answer""")
        startCheck()


itemsPurchased = []

def displayCodeTerminal():
    print("╔═════════════════╗")
    print("║  SELECT PRODUCT ║")
    print("║       CODE      ║")
    print("║                 ║")
    print("║     >           ║")
    print("║                 ║")
    print("╚═════════════════╝")

    print("\033[3A\033[9C", end="")
    global codeInput
    codeInput = input("").upper()
    print("")
    print("")

    priceVer = balance - (products[codeInput]["price"])
    if codeInput in products:
        if priceVer < 0:
            print("Not enough money")
            continueCheck()
        else:
            itemsPurchased.append(codeInput)
            print("product found")
            productInfoTerminal()
            itemsPurchased.append(codeInput)
        
    else:
        print("""product not found
try again""")
        displayCodeTerminal()


def productInfoTerminal():
    product = products[codeInput]
    global balance
    newBalance = balance - product["price"]
    print("╔════════════════════════╗")
    print(f"║     {product["name"]:<17}  ║")
    print("║                        ║")
    print(f"║     {('$' + format(product['price'], '.2f')):<19}║")
    print("║                        ║")
    print("║       New Balance:     ║")
    print("║                        ║")
    print(f"║        {'$' + str(newBalance):<16}║")
    print("║                        ║")
    print("╚════════════════════════╝")

    balance = newBalance
    continueCheck()
    return balance



def continueCheck():
    continueInput = input("""Do you want to add more products? yes/no
""").lower()
    if continueInput == "yes":
        displayCodeTerminal()
    elif continueInput == "no":
        dispenseItems()
        print("Purchase ended")
    else:
        print("Invalid input, Try again")
        continueCheck()

def addMoneyTerminal():
    print("╔══════════════╗")
    print("║   Add Money  ║")
    print("║              ║")
    print("║    >$        ║")
    print("║              ║")
    print("╚══════════════╝")
    print("\033[3A\033[7C", end="")
    global moneyInput
    try:
        moneyInput = int(input(""))
        print("")
        print("")
        print("")
        moneyCheck()
    except:
        print("")
        print("")
        print("")
        print("Enter a valid amount")
        addMoneyTerminal()
    print("")
    print("")
    print("")


def moneyCheck():
    global balance
    if moneyInput >= 1000:
        print("""Be realistic, You DON'T have that much money
Try again""")
        addMoneyTerminal()
    elif moneyInput <= 0:
        print("You need to actually add money")
        addMoneyTerminal()
    else:
        balance += moneyInput
        displayTerminalBalance()

def dispenseItems():
    print("╔══════════════════════╗")
    print("║   Items Purchased:   ║")
    print("║                      ║")
    for item in itemsPurchased:
        print(f"║ -{products[item]["name"]:<20}║")
    print("║                      ║")
    print("║       Change:        ║")
    print(f"║       {balance:<15}║")
    print("║                      ║")
    print("╚══════════════════════╝")

"""
!CODE UNDER CONSTRUCTION!
"""


displayProducts()
addMoneyTerminal()
startCheck()