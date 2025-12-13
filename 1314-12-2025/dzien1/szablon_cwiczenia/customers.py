"""
Moduł zarządzania klientami pizzerii.
"""

# TODO: Utwórz globalną listę customers
# customers = []

# TODO: Utwórz zmienną globalną next_customer_id = 1


# TODO: Zaimplementuj funkcję add_customer(name, phone)
# Powinna:
# - Zadeklarować: global next_customer_id
# - Utworzyć słownik {'id': next_customer_id, 'name': name, 'phone': phone}
# - Dodać go do listy customers
# - Wyświetlić komunikat z ID
# - Zwiększyć next_customer_id o 1
# - Zwrócić ID klienta


# TODO: Zaimplementuj funkcję find_customer(customer_id)
# Powinna:
# - Iterować po liście customers
# - Znaleźć klienta o danym ID
# - Zwrócić słownik klienta lub None


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
