# Przykład testów jednostkowych z pytest

import pytest
from pizza import Pizza, Menu
from customer import Customer, VIPCustomer
from order import Order, OrderItem
from exceptions import InvalidPriceError, InvalidQuantityError

class TestPizza:
    def test_pizza_creation(self):
        pizza = Pizza("Margherita", 25.0)
        assert pizza.name == "Margherita"
        assert pizza.price == 25.0

    def test_pizza_invalid_price(self):
        with pytest.raises(ValueError):
            Pizza("Test", 0)

    def test_pizza_str(self):
        pizza = Pizza("Pepperoni", 30.0)
        assert str(pizza) == "Pepperoni: 30.0 zł"

    def test_pizza_equality(self):
        pizza1 = Pizza("Test", 20.0)
        pizza2 = Pizza("Test", 20.0)
        pizza3 = Pizza("Test", 25.0)
        assert pizza1 == pizza2
        assert pizza1 != pizza3

class TestMenu:
    def test_menu_add_pizza(self):
        menu = Menu()
        pizza = Pizza("Test", 20.0)
        menu.add_pizza(pizza)
        assert len(menu) == 1
        assert menu.find_pizza("Test") == pizza

    def test_menu_remove_pizza(self):
        menu = Menu()
        pizza = Pizza("Test", 20.0)
        menu.add_pizza(pizza)
        menu.remove_pizza("Test")
        assert len(menu) == 0

    def test_menu_remove_nonexistent_pizza(self):
        menu = Menu()
        with pytest.raises(ValueError):
            menu.remove_pizza("Nonexistent")

class TestCustomer:
    def test_customer_creation(self):
        customer = Customer("Jan Kowalski", "123-456-789")
        assert customer.name == "Jan Kowalski"
        assert customer.phone == "123-456-789"
        assert customer.id is not None

    def test_customer_str(self):
        customer = Customer("Jan Kowalski", "123-456-789")
        assert "Jan Kowalski" in str(customer)

class TestVIPCustomer:
    def test_vip_customer_creation(self):
        vip = VIPCustomer("Anna Nowak", "987-654-321", 15)
        assert vip.discount_percent == 15
        assert vip.loyalty_points == 0

    def test_vip_discount(self):
        vip = VIPCustomer("Anna Nowak", "987-654-321", 10)
        assert vip.apply_discount(100) == 90

    def test_inheritance(self):
        vip = VIPCustomer("Test", "123", 5)
        assert isinstance(vip, Customer)

class TestOrderItem:
    def test_order_item_creation(self):
        pizza = Pizza("Test", 20.0)
        item = OrderItem(pizza, 2)
        assert item.quantity == 2
        assert item.total_price == 40.0

    def test_order_item_invalid_quantity(self):
        pizza = Pizza("Test", 20.0)
        with pytest.raises(ValueError):
            OrderItem(pizza, 0)

class TestOrder:
    def test_order_creation(self):
        customer = Customer("Test", "123")
        order = Order(customer)
        assert order.customer == customer
        assert len(order) == 0

    def test_order_add_item(self):
        customer = Customer("Test", "123")
        order = Order(customer)
        pizza = Pizza("Test", 20.0)
        order.add_item(pizza, 1)
        assert len(order) == 1
        assert order.total_price == 20.0

# Uruchomienie testów: pytest test_example.py -v