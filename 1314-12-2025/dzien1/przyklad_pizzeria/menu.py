# Moduł menu - zarządzanie menu pizzerii

pizzas = []  # Lista pizz w menu

def add_pizza(name, price):
    """
    Dodaje pizzę do menu.

    Args:
        name (str): Nazwa pizzy
        price (float): Cena pizzy
    """
    pizza = {'name': name, 'price': price}
    pizzas.append(pizza)
    print(f"Dodano pizzę: {name} za {price} zł")

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
        print(f"- {pizza['name']}: {pizza['price']} zł")

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