# Moduł menu - zarządzanie menu pizzerii

class Pizza:
    def __init__(self, name, price):
        if price <= 0:
            raise ValueError("Cena musi byc > 0")
        self.__name = name
        self.__price = price

    def name(self):
        return self.__name

    def price(self):
        return self.__price

pizzas = []  # Lista pizz w menu

def add_pizza(pizza):
    pizzas.append(pizza)
    print(f"Dodano pizzę: {pizza.name()} za {pizza.price()} zł")

def remove_pizza(name):
    """
    Usuwa pizzę z menu.

    Args:
        name (str): Nazwa pizzy do usunięcia
    """
    global pizzas
    pizzas = [p for p in pizzas if p['name'] != name]
    print(f"Usunięto pizzę: {name}")

def list_pizzas():
    """
    Wyświetla wszystkie pizze w menu.
    """
    if not pizzas:
        print("Menu jest puste.")
        return
    print("Menu pizzerii:")
    for pizza in pizzas:
        print(f"- {pizza.name()}: {pizza.price()} zł")

def find_pizza(name):
    """
    Znajduje pizzę po nazwie.

    Args:
        name (str): Nazwa pizzy

    Returns:
        dict or None: Słownik z danymi pizzy lub None jeśli nie znaleziono
    """
    for pizza in pizzas:
        if pizza['name'] == name:
            return pizza
    return None
