"""
Moduł zarządzania zamówieniami.
"""

# TODO: Zaimportuj moduł menu
# from . import menu

# TODO: Utwórz globalną listę orders
# orders = []

# TODO: Utwórz zmienną globalną next_order_id = 1


# TODO: Zaimplementuj funkcję create_order(customer_id)
# Powinna:
# - Zadeklarować: global next_order_id
# - Utworzyć słownik {'id': next_order_id, 'customer_id': customer_id, 'items': []}
# - Dodać go do listy orders
# - Wyświetlić komunikat
# - Zwiększyć next_order_id o 1
# - Zwrócić ID zamówienia


# TODO: Zaimplementuj funkcję find_order(order_id)
# Powinna:
# - Iterować po liście orders
# - Znaleźć zamówienie o danym ID
# - Zwrócić słownik zamówienia lub None


# TODO: Zaimplementuj funkcję add_item_to_order(order_id, pizza_name, quantity)
# Powinna:
# - Znaleźć zamówienie (użyj find_order)
# - Jeśli nie ma - wyświetlić błąd i zwrócić False
# - Znaleźć pizzę w menu (użyj menu.find_pizza)
# - Jeśli nie ma - wyświetlić błąd i zwrócić False
# - Utworzyć słownik pozycji: {'pizza_name': ..., 'price': pizza['price'], 'quantity': ...}
# - Dodać pozycję do order['items']
# - Wyświetlić komunikat
# - Zwrócić True


# TODO: Zaimplementuj funkcję list_order(order_id)
# Powinna:
# - Znaleźć zamówienie
# - Jeśli nie ma - wyświetlić błąd
# - Wyświetlić nagłówek z ID zamówienia
# - Wyświetlić customer_id
# - Iterować po items i dla każdego wyświetlić: quantity x pizza_name = subtotal
# - Obliczyć i wyświetlić RAZEM


# BONUS: Zaimplementuj funkcję remove_item_from_order(order_id, pizza_name)
# Powinna:
# - Znaleźć zamówienie
# - Znaleźć pozycję z daną pizzą w order['items']
# - Usunąć ją z listy
# - Wyświetlić komunikat
