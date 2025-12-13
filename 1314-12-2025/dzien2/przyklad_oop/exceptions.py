# Własne wyjątki dla aplikacji pizzerii

class PizzeriaError(Exception):
    """Bazowa klasa wyjątków dla pizzerii"""
    pass

class PizzaNotFoundError(PizzeriaError):
    """Wyjątek rzucany gdy pizza nie została znaleziona"""
    def __init__(self, pizza_name):
        self.pizza_name = pizza_name
        super().__init__(f"Pizza '{pizza_name}' nie została znaleziona w menu")

class CustomerNotFoundError(PizzeriaError):
    """Wyjątek rzucany gdy klient nie został znaleziony"""
    def __init__(self, customer_id):
        self.customer_id = customer_id
        super().__init__(f"Klient o ID {customer_id} nie został znaleziony")

class OrderNotFoundError(PizzeriaError):
    """Wyjątek rzucany gdy zamówienie nie zostało znalezione"""
    def __init__(self, order_id):
        self.order_id = order_id
        super().__init__(f"Zamówienie o ID {order_id} nie zostało znalezione")

class InvalidPriceError(PizzeriaError):
    """Wyjątek rzucany gdy cena jest nieprawidłowa"""
    def __init__(self, price):
        self.price = price
        super().__init__(f"Cena {price} jest nieprawidłowa (musi być > 0)")

class InvalidQuantityError(PizzeriaError):
    """Wyjątek rzucany gdy ilość jest nieprawidłowa"""
    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__(f"Ilość {quantity} jest nieprawidłowa (musi być > 0)")