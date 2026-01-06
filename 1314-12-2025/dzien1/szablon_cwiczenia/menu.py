"""
Moduł zarządzania menu pizzerii.
"""

menu = []

def add_pizza(name, price):
    pizza = {
        'name': name,
        'price': price
    }
    menu.append(pizza)
    print(f"Dodano: {name} za {price} zl")

def list_menu():
    if not menu: #lista pusta: Node.js = True, C++ = True, w Pythonie = False
        print("Menu jest puste!")
        return

    print("=== MENU ===")
    for pizza in menu:
        print(f"{pizza['name']}: {pizza['price']} zl")

def find_pizza(name):
    for pizza in menu:
        if pizza['name'] == name:
            return pizza
    return None

# BONUS: Zaimplementuj funkcję update_pizza_price(name, new_price)
# Powinna:
# - Znaleźć pizzę (użyj find_pizza)
# - Zaktualizować jej cenę
# - Wyświetlić komunikat
