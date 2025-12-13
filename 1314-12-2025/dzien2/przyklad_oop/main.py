# Główny plik aplikacji pizzerii OOP - demonstracja użycia klas

from pizza import Pizza, Menu
from customer import Customer, VIPCustomer, CustomerManager
from order import Order, OrderManager
from exceptions import PizzeriaError

def main():
    print("Witaj w aplikacji pizzerii OOP!")

    # Tworzymy menu
    menu = Menu()
    try:
        pizza1 = Pizza("Margherita", 25.0)
        pizza2 = Pizza("Pepperoni", 30.0)
        pizza3 = Pizza("Hawajska", 32.0)

        menu.add_pizza(pizza1)
        menu.add_pizza(pizza2)
        menu.add_pizza(pizza3)
    except ValueError as e:
        print(f"Błąd podczas tworzenia pizzy: {e}")
        return

    print(f"\nMenu zawiera {len(menu)} pizz:")
    menu.list_pizzas()

    # Tworzymy manager klientów
    customer_manager = CustomerManager()
    customer1 = Customer("Jan Kowalski", "123-456-789")
    vip_customer = VIPCustomer("Anna Nowak", "987-654-321", 15)

    customer_manager.add_customer(customer1)
    customer_manager.add_customer(vip_customer)

    print(f"\nLista klientów ({len(customer_manager)}):")
    customer_manager.list_customers()

    # Tworzymy manager zamówień
    order_manager = OrderManager()

    # Zamówienie dla zwykłego klienta
    order1 = order_manager.create_order(customer1)
    order1.add_item(pizza1, 2)
    order1.add_item(pizza2, 1)

    # Zamówienie dla VIP klienta
    order2 = order_manager.create_order(vip_customer)
    order2.add_item(pizza3, 1)
    vip_customer.add_loyalty_points(10)  # Dodajemy punkty lojalnościowe

    print(f"\nSzczegóły zamówienia 1:\n{order1}")
    print(f"\nSzczegóły zamówienia 2:\n{order2}")

    print(f"\nWszystkie zamówienia ({len(order_manager)}):")
    order_manager.list_orders()

    # Demonstracja obsługi wyjątków
    try:
        menu.find_pizza("Nieistniejąca Pizza")
    except PizzeriaError as e:
        print(f"\nPrzechwycono wyjątek: {e}")

    # Demonstracja metod specjalnych
    print(f"\nPorównanie pizz: {pizza1 == Pizza('Margherita', 25.0)}")
    print(f"Reprezentacja pizzy: {repr(pizza1)}")

if __name__ == "__main__":
    main()