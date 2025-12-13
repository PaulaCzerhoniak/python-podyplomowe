# Klasy Order - reprezentują zamówienia

from pizza import Pizza
from customer import Customer

class OrderItem:
    def __init__(self, pizza, quantity):
        if not isinstance(pizza, Pizza):
            raise TypeError("Pizza musi być instancją klasy Pizza")
        if quantity <= 0:
            raise ValueError("Ilość musi być większa od zera")
        self.pizza = pizza
        self.quantity = quantity

    @property
    def total_price(self):
        return self.pizza.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.pizza.name} ({self.total_price} zł)"

class Order:
    _next_id = 1

    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Customer musi być instancją klasy Customer")
        self.customer = customer
        self.items = []
        self.id = Order._next_id
        Order._next_id += 1

    def add_item(self, pizza, quantity):
        item = OrderItem(pizza, quantity)
        self.items.append(item)
        print(f"Dodano do zamówienia: {item}")

    def remove_item(self, pizza_name):
        for item in self.items:
            if item.pizza.name == pizza_name:
                self.items.remove(item)
                print(f"Usunięto z zamówienia: {pizza_name}")
                return
        raise ValueError(f"Pozycja {pizza_name} nie znaleziona w zamówieniu")

    @property
    def total_price(self):
        total = sum(item.total_price for item in self.items)
        # Zastosuj zniżkę dla VIP
        if hasattr(self.customer, 'apply_discount'):
            total = self.customer.apply_discount(total)
        return total

    def __str__(self):
        items_str = "\n".join(f"  - {item}" for item in self.items)
        return f"Zamówienie ID: {self.id}\nKlient: {self.customer.name}\nPozycje:\n{items_str}\nŁącznie: {self.total_price} zł"

    def __len__(self):
        return len(self.items)

# Klasa OrderManager - zarządza zamówieniami
class OrderManager:
    def __init__(self):
        self.orders = []

    def create_order(self, customer):
        order = Order(customer)
        self.orders.append(order)
        print(f"Utworzono {order}")
        return order

    def cancel_order(self, order_id):
        for order in self.orders:
            if order.id == order_id:
                self.orders.remove(order)
                print(f"Anulowano zamówienie ID: {order_id}")
                return
        raise ValueError(f"Zamówienie o ID {order_id} nie znalezione")

    def find_order(self, order_id):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None

    def list_orders(self):
        if not self.orders:
            print("Brak zamówień.")
            return
        print("Wszystkie zamówienia:")
        for order in self.orders:
            print(f"- ID: {order.id}, Klient: {order.customer.name}, Łącznie: {order.total_price} zł")

    @staticmethod
    def calculate_total_revenue():
        # Przykład metody statycznej
        return sum(order.total_price for order in OrderManager().orders)  # W rzeczywistości trzeba przekazać instancję

    def __len__(self):
        return len(self.orders)