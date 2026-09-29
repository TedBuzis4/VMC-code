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
    print(f"║     ${balance}      ║")
    print("║             ║")
    print("╚═════════════╝")

def startCheck():
    if startInput == "yes":
        print()
    elif startInput == "no":
        print("Operation Ended")
    else:
        print("Invalid input" \
        "Type a valid answer")



displayProducts()
displayTerminalBalance()
startInput = input("""Do you want to start the purchace? yes/no
""")