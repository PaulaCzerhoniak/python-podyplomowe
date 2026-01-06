# Klasy Customer - reprezentują klientów


class Customer:
    __next_id = 1  # Klasowa zmienna do generowania ID
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.id = Customer.__next_id
        Customer.__next_id += 1

    def __str__(self):
        return f"Klient {self.id}: {self.name}, tel: {self.phone}"

    def __repr__(self):
        return f"Customer(name='{self.name}', phone='{self.phone}', id={self.id})"

    def update_phone(self, new_phone):
        self.phone = new_phone

    def discount_percent(self):
        return 0

    @classmethod
    def reset_id_counter(cls):
        cls._next_id = 1

class VIPCustomer(Customer):
    def __init__(self, name, phone, discount_percent):
        super().__init__(name, phone)  # Konstruktor rodzica
        self.__discount_percent = discount_percent

    def discount_percent(self):
        return self.__discount_percent

    def __str__(self):
        return f"Klient {self.id}: {self.name}, tel: {self.phone}. UWAGA, Klient VIP!: discount {self.__discount_percent}"
