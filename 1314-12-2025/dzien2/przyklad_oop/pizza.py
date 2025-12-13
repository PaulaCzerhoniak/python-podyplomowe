# Klasa Pizza - reprezentuje pizzę w menu

class Pizza:
    def __init__(self, name, price):
        if price <= 0:
            raise ValueError("Cena musi być większa od zera")
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} zł"

    def __repr__(self):
        return f"Pizza(name='{self.name}', price={self.price})"

    def __eq__(self, other):
        if isinstance(other, Pizza):
            return self.name == other.name and self.price == other.price
        return False

    def update_price(self, new_price):
        if new_price <= 0:
            raise ValueError("Cena musi być większa od zera")
        self.price = new_price

# Klasa Menu - zarządza kolekcją pizz
class Menu:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("Obiekt musi być instancją klasy Pizza")
        self.pizzas.append(pizza)
        print(f"Dodano pizzę: {pizza}")

    def remove_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                print(f"Usunięto pizzę: {name}")
                return
        raise ValueError(f"Pizza {name} nie znaleziona w menu")

    def find_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                return pizza
        return None

    def list_pizzas(self):
        if not self.pizzas:
            print("Menu jest puste.")
            return
        print("Menu pizzerii:")
        for pizza in self.pizzas:
            print(f"- {pizza}")

    def __len__(self):
        return len(self.pizzas)