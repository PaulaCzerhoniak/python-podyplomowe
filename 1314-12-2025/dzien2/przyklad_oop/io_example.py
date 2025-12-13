# Przykład operacji wejścia/wyjścia (I/O)

import json
from pizza import Menu, Pizza
from customer import CustomerManager, Customer
from order import OrderManager

def save_menu_to_file(menu, filename="menu.json"):
    """Zapisuje menu do pliku JSON"""
    menu_data = [{"name": pizza.name, "price": pizza.price} for pizza in menu.pizzas]
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(menu_data, f, ensure_ascii=False, indent=2)
    print(f"Menu zapisane do {filename}")

def load_menu_from_file(filename="menu.json"):
    """Wczytuje menu z pliku JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            menu_data = json.load(f)
        menu = Menu()
        for item in menu_data:
            pizza = Pizza(item['name'], item['price'])
            menu.add_pizza(pizza)
        print(f"Menu wczytane z {filename}")
        return menu
    except FileNotFoundError:
        print(f"Plik {filename} nie istnieje")
        return Menu()
    except json.JSONDecodeError:
        print(f"Błąd w formacie pliku {filename}")
        return Menu()

def save_orders_to_csv(order_manager, filename="orders.csv"):
    """Zapisuje zamówienia do pliku CSV"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("OrderID,CustomerName,TotalPrice\n")
        for order in order_manager.orders:
            f.write(f"{order.id},{order.customer.name},{order.total_price}\n")
    print(f"Zamówienia zapisane do {filename}")

def read_text_file(filename):
    """Czyta cały plik tekstowy"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"Plik {filename} nie istnieje"

def write_text_file(filename, content):
    """Zapisuje tekst do pliku"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Tekst zapisany do {filename}")

def demonstrate_io():
    """Demonstracja operacji I/O"""
    print("=== Demonstracja operacji I/O ===")

    # Tworzymy przykładowe dane
    menu = Menu()
    menu.add_pizza(Pizza("Margherita", 25.0))
    menu.add_pizza(Pizza("Pepperoni", 30.0))

    customer_manager = CustomerManager()
    customer_manager.add_customer(Customer("Jan Kowalski", "123-456-789"))

    order_manager = OrderManager()
    order = order_manager.create_order(customer_manager.customers[0])
    order.add_item(menu.pizzas[0], 2)

    # Zapis i odczyt menu
    save_menu_to_file(menu)
    loaded_menu = load_menu_from_file()
    loaded_menu.list_pizzas()

    # Zapis zamówień do CSV
    save_orders_to_csv(order_manager)

    # Przykład czytania/zapisywania tekstu
    sample_text = "To jest przykładowy tekst do zapisania w pliku.\nDruga linia tekstu."
    write_text_file("sample.txt", sample_text)
    read_content = read_text_file("sample.txt")
    print(f"Odczytany tekst:\n{read_content}")

if __name__ == "__main__":
    demonstrate_io()