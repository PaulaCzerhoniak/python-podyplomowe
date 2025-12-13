# Moduł customers - zarządzanie klientami

customers = []  # Lista klientów

def add_customer(name, phone):
    """
    Dodaje klienta.

    Args:
        name (str): Imię i nazwisko klienta
        phone (str): Numer telefonu
    """
    customer = {'name': name, 'phone': phone, 'id': len(customers) + 1}
    customers.append(customer)
    print(f"Dodano klienta: {name}, ID: {customer['id']}")
    return customer['id']

def remove_customer(customer_id):
    """
    Usuwa klienta po ID.

    Args:
        customer_id (int): ID klienta
    """
    global customers
    customers = [c for c in customers if c['id'] != customer_id]
    print(f"Usunięto klienta o ID: {customer_id}")

def list_customers():
    """
    Wyświetla wszystkich klientów.
    """
    if not customers:
        print("Brak klientów.")
        return
    print("Lista klientów:")
    for customer in customers:
        print(f"- ID: {customer['id']}, {customer['name']}, tel: {customer['phone']}")

def find_customer(customer_id):
    """
    Znajduje klienta po ID.

    Args:
        customer_id (int): ID klienta

    Returns:
        dict or None: Słownik z danymi klienta lub None jeśli nie znaleziono
    """
    for customer in customers:
        if customer['id'] == customer_id:
            return customer
    return None