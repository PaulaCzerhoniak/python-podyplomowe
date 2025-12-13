# Klasy Customer - reprezentują klientów

class Customer:
    _next_id = 1  # Klasowa zmienna do generowania ID

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.id = Customer._next_id
        Customer._next_id += 1

    def __str__(self):
        return f"Klient {self.id}: {self.name}, tel: {self.phone}"

    def __repr__(self):
        return f"Customer(name='{self.name}', phone='{self.phone}', id={self.id})"

    def update_phone(self, new_phone):
        self.phone = new_phone

    @classmethod
    def reset_id_counter(cls):
        cls._next_id = 1

# Dziedziczenie: VIP Customer z dodatkowymi korzyściami
class VIPCustomer(Customer):
    def __init__(self, name, phone, discount_percent=10):
        super().__init__(name, phone)
        self.discount_percent = discount_percent
        self.loyalty_points = 0

    def __str__(self):
        return f"VIP {super().__str__()}, zniżka: {self.discount_percent}%, punkty: {self.loyalty_points}"

    def add_loyalty_points(self, points):
        self.loyalty_points += points

    def apply_discount(self, amount):
        return amount * (1 - self.discount_percent / 100)

# Klasa CustomerManager - zarządza klientami
class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Obiekt musi być instancją klasy Customer lub jej podklasy")
        self.customers.append(customer)
        print(f"Dodano {customer}")

    def remove_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                self.customers.remove(customer)
                print(f"Usunięto klienta ID: {customer_id}")
                return
        raise ValueError(f"Klient o ID {customer_id} nie znaleziony")

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def list_customers(self):
        if not self.customers:
            print("Brak klientów.")
            return
        print("Lista klientów:")
        for customer in self.customers:
            print(f"- {customer}")

    def __len__(self):
        return len(self.customers)