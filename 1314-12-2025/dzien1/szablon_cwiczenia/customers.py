"""
Moduł zarządzania klientami pizzerii.
"""

customers = []
next_customer_id = 1

def add_customer(name, phone):
    global next_customer_id
    customerId = next_customer_id
    customer = {
        'id': customerId,
        'name': name,
        'phone': phone
    }
    customers.append(customer)
    print(f'Dodano klienta, id: {customerId}')
    next_customer_id += 1
    return customerId

# TODO: Zaimplementuj funkcję find_customer(customer_id)
# Powinna:
# - Iterować po liście customers
# - Znaleźć klienta o danym ID
# - Zwrócić słownik klienta lub None
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

# TODO: Zaimplementuj funkcję list_customers()
# Powinna:
# - Sprawdzić czy lista nie jest pusta
# - Wyświetlić nagłówek "=== KLIENCI ==="
# - Iterować po klientach i wyświetlić w formacie: [ID] Imię - Telefon


# BONUS: Zaimplementuj funkcję update_customer_phone(customer_id, new_phone)
# Powinna:
# - Znaleźć klienta (użyj find_customer)
# - Zaktualizować telefon
# - Wyświetlić komunikat
