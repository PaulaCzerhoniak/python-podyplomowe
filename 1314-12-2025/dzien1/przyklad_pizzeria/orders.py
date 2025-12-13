# Moduł orders - zarządzanie zamówieniami

import menu
import customers

orders = []  # Lista zamówień

def create_order(customer_id):
    """
    Tworzy nowe zamówienie dla klienta.

    Args:
        customer_id (int): ID klienta

    Returns:
        int: ID zamówienia
    """
    customer = customers.find_customer(customer_id)
    if not customer:
        print("Klient nie znaleziony.")
        return None
    order = {
        'id': len(orders) + 1,
        'customer_id': customer_id,
        'items': [],  # Lista słowników: {'pizza_name': str, 'quantity': int}
        'total': 0.0
    }
    orders.append(order)
    print(f"Utworzono zamówienie ID: {order['id']} dla klienta {customer['name']}")
    return order['id']

def add_item_to_order(order_id, pizza_name, quantity):
    """
    Dodaje pozycję do zamówienia.

    Args:
        order_id (int): ID zamówienia
        pizza_name (str): Nazwa pizzy
        quantity (int): Ilość
    """
    order = find_order(order_id)
    if not order:
        print("Zamówienie nie znalezione.")
        return
    pizza = menu.find_pizza(pizza_name)
    if not pizza:
        print("Pizza nie znaleziona w menu.")
        return
    item = {'pizza_name': pizza_name, 'quantity': quantity, 'price': pizza['price']}
    order['items'].append(item)
    order['total'] += quantity * pizza['price']
    print(f"Dodano do zamówienia: {quantity}x {pizza_name}")

def remove_item_from_order(order_id, pizza_name):
    """
    Usuwa pozycję z zamówienia.

    Args:
        order_id (int): ID zamówienia
        pizza_name (str): Nazwa pizzy do usunięcia
    """
    order = find_order(order_id)
    if not order:
        print("Zamówienie nie znalezione.")
        return
    for item in order['items']:
        if item['pizza_name'] == pizza_name:
            order['total'] -= item['quantity'] * item['price']
            order['items'].remove(item)
            print(f"Usunięto z zamówienia: {pizza_name}")
            return
    print("Pozycja nie znaleziona w zamówieniu.")

def list_order(order_id):
    """
    Wyświetla szczegóły zamówienia.

    Args:
        order_id (int): ID zamówienia
    """
    order = find_order(order_id)
    if not order:
        print("Zamówienie nie znalezione.")
        return
    customer = customers.find_customer(order['customer_id'])
    print(f"Zamówienie ID: {order['id']}")
    print(f"Klient: {customer['name']}")
    print("Pozycje:")
    for item in order['items']:
        print(f"- {item['quantity']}x {item['pizza_name']}: {item['quantity'] * item['price']} zł")
    print(f"Łącznie: {order['total']} zł")

def find_order(order_id):
    """
    Znajduje zamówienie po ID.

    Args:
        order_id (int): ID zamówienia

    Returns:
        dict or None: Słownik z danymi zamówienia lub None jeśli nie znaleziono
    """
    for order in orders:
        if order['id'] == order_id:
            return order
    return None

def list_all_orders():
    """
    Wyświetla wszystkie zamówienia.
    """
    if not orders:
        print("Brak zamówień.")
        return
    print("Wszystkie zamówienia:")
    for order in orders:
        customer = customers.find_customer(order['customer_id'])
        print(f"- ID: {order['id']}, Klient: {customer['name']}, Łącznie: {order['total']} zł")