# Główny plik aplikacji pizzerii - demonstracja użycia modułów

import menu
import customers
import orders

def main():
    print("Witaj w aplikacji pizzerii!")

    # Dodajemy pizze do menu
    menu.add_pizza(menu.Pizza("Margherita", 25.0))
    menu.add_pizza(menu.Pizza("Pepperoni", 30.0))
    menu.add_pizza(menu.Pizza("Hawajska", 32.0))

    print("\nAktualne menu:")
    menu.list_pizzas()

#    # Dodajemy klientów
#    cust1_id = customers.add_customer("Jan Kowalski", "123-456-789")
#    cust2_id = customers.add_customer("Anna Nowak", "987-654-321")
#
#    print("\nLista klientów:")
#    customers.list_customers()
#
#    # Tworzymy zamówienia
#    order1_id = orders.create_order(cust1_id)
#    if order1_id:
#        orders.add_item_to_order(order1_id, "Margherita", 2)
#        orders.add_item_to_order(order1_id, "Pepperoni", 1)
#
#    order2_id = orders.create_order(cust2_id)
#    if order2_id:
#        orders.add_item_to_order(order2_id, "Hawajska", 1)
#
#    print("\nSzczegóły zamówienia 1:")
#    orders.list_order(order1_id)
#
#    print("\nWszystkie zamówienia:")
#    orders.list_all_orders()

if __name__ == "__main__":
    main()
