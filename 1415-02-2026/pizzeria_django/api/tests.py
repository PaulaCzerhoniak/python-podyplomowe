import pytest
from rest_framework.test import APIClient
from menu_app.models import Pizza
from customers_app.models import Customer
from orders_app.models import Order, OrderItem


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def sample_pizza():
    return Pizza.objects.create(name="Margherita", price=25.0)

@pytest.fixture
def sample_customer(db):
    return Customer.objects.create(
        first_name="Jan",
        last_name="Kowalski",
        phone="123456789",
        customer_type="regular",
        discount_percent=0
    )
    
@pytest.fixture
def sample_order(db, sample_customer, sample_pizza):
    order = Order.objects.create(customer=sample_customer)
    OrderItem.objects.create(order=order, pizza=sample_pizza, quantity=2)
    return order


# === Testy Pizza API ===

class TestPizzaAPI:

    @pytest.mark.django_db
    def test_list_empty(self, api_client):
        """GET /api/pizzas/ zwraca pusta liste gdy brak pizz."""
        response = api_client.get('/api/pizzas/')
        assert response.status_code == 200
        assert response.data == []

    @pytest.mark.django_db
    def test_list_with_data(self, api_client, sample_pizza):
        """GET /api/pizzas/ zwraca liste pizz."""
        response = api_client.get('/api/pizzas/')
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]['name'] == 'Margherita'

    @pytest.mark.django_db
    def test_detail(self, api_client, sample_pizza):
        """GET /api/pizzas/<name>/ zwraca szczegoly pizzy."""
        response = api_client.get('/api/pizzas/Margherita/')
        assert response.status_code == 200
        assert response.data['name'] == 'Margherita'
        assert response.data['price'] == 25.0

    @pytest.mark.django_db
    def test_detail_not_found(self, api_client):
        """GET /api/pizzas/<name>/ zwraca 404 dla nieistniejacej pizzy."""
        response = api_client.get('/api/pizzas/NieIstniejaca/')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_create(self, api_client):
        """POST /api/pizzas/ tworzy nowa pizze."""
        response = api_client.post('/api/pizzas/', {
            'name': 'Diavola',
            'price': 34.0,
        }, format='json')
        assert response.status_code == 201
        assert response.data['name'] == 'Diavola'
        assert Pizza.objects.count() == 1

    @pytest.mark.django_db
    def test_create_invalid(self, api_client):
        """POST /api/pizzas/ z blednymi danymi zwraca 400."""
        response = api_client.post('/api/pizzas/', {
            'name': '',
            'price': 34.0,
        }, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_duplicate(self, api_client, sample_pizza):
        """POST /api/pizzas/ z duplikatem nazwy zwraca 400."""
        response = api_client.post('/api/pizzas/', {
            'name': 'Margherita',
            'price': 99.0,
        }, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update(self, api_client, sample_pizza):
        """PUT /api/pizzas/<name>/ aktualizuje pizze."""
        response = api_client.put('/api/pizzas/Margherita/', {
            'name': 'Margherita',
            'price': 28.0,
        }, format='json')
        assert response.status_code == 200
        assert response.data['price'] == 28.0

    @pytest.mark.django_db
    def test_delete(self, api_client, sample_pizza):
        """DELETE /api/pizzas/<name>/ usuwa pizze."""
        response = api_client.delete('/api/pizzas/Margherita/')
        assert response.status_code == 204
        assert Pizza.objects.count() == 0
        
# ========================
# Testy Customer API
# ========================
@pytest.mark.django_db
class TestCustomerAPI:

    def test_list_empty(self, api_client):
        response = api_client.get('/api/customers/')
        assert response.status_code == 200
        assert response.data == []

    def test_list_with_data(self, api_client, sample_customer):
        response = api_client.get('/api/customers/')
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]['first_name'] == 'Jan'

    def test_detail(self, api_client, sample_customer):
        response = api_client.get(f'/api/customers/{sample_customer.id}/')
        assert response.status_code == 200
        assert response.data['first_name'] == 'Jan'
        assert response.data['last_name'] == 'Kowalski'

    def test_create(self, api_client):
        response = api_client.post('/api/customers/', {
            'first_name': 'Anna',
            'last_name': 'Nowak',
            'phone': '987654321',
            'customer_type': 'vip',
            'discount_percent': 10
        }, format='json')
        assert response.status_code == 201
        assert Customer.objects.count() == 1

# ========================
# Testy Order API
# ========================
@pytest.mark.django_db
class TestOrderAPI:

    def test_list_empty(self, api_client):
        response = api_client.get('/api/orders/')
        assert response.status_code == 200
        assert response.data == []

    def test_create_order(self, api_client, sample_customer, sample_pizza):
        data = {
            'customer_id': sample_customer.id,
            'items': [{'pizza_id': sample_pizza.id, 'quantity': 3}]
        }
        response = api_client.post('/api/orders/', data, format='json')
        assert response.status_code == 201
        assert response.data['customer_name'] == f"{sample_customer.first_name} {sample_customer.last_name}"
        assert len(response.data['items']) == 1
        assert response.data['items'][0]['subtotal'] == sample_pizza.price * 3

    def test_detail(self, api_client, sample_order):
        response = api_client.get(f'/api/orders/{sample_order.id}/')
        assert response.status_code == 200
        assert response.data['id'] == sample_order.id

    def test_delete(self, api_client, sample_order):
        response = api_client.delete(f'/api/orders/{sample_order.id}/')
        assert response.status_code == 204
        assert Order.objects.count() == 0