from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from menu_app.models import Pizza
from customers_app.models import Customer
from orders_app.models import Order
from .serializers import PizzaSerializer, CustomerSerializer, OrderSerializer, OrderCreateSerializer

@api_view(['GET', 'POST'])
def pizza_list_api(request):
    """
    GET /api/pizzas/ - lista wszystkich pizz
        ?search=<tekst>   -> wyszukiwanie po nazwie (name__icontains)
        ?ordering=<pole>  -> sortowanie po polu, np. price, -price, name
    POST /api/pizzas/ - dodaj nową pizze
    """
    if request.method == 'GET':
        # 1️⃣ Wyszukiwanie
        search = request.query_params.get('search')
        if search:
            pizzas = Pizza.objects.filter(name__icontains=search)
        else:
            pizzas = Pizza.objects.all()

        # 2️⃣ Sortowanie
        ordering = request.query_params.get('ordering')
        if ordering:
            pizzas = pizzas.order_by(ordering)

        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pizza_detail_api(request, name):
    """
    GET    /api/pizzas/<name>/ - szczegoly pizzy
    PUT    /api/pizzas/<name>/ - aktualizuj pizze
    DELETE /api/pizzas/<name>/ - usun pizze
    """
    try:
        pizza = Pizza.objects.get(name=name)
    except Pizza.DoesNotExist:
        return Response(
            {"error": f"Pizza '{name}' nie znaleziona"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = PizzaSerializer(pizza)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def customer_list_api(request):
    """
    GET /api/customers/ - lista wszystkich klientów
        ?search=<tekst>    -> wyszukiwanie po first_name lub last_name
        ?ordering=<pole>   -> sortowanie po polu: first_name, last_name, loyalty_points
    POST /api/customers/ - dodaj nowego klienta
    """
    if request.method == 'GET':
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')

        # 1️⃣ Filtrowanie po first_name / last_name
        if search:
            customers = Customer.objects.filter(
                first_name__icontains=search
            ) | Customer.objects.filter(
                last_name__icontains=search
            )
        else:
            customers = Customer.objects.all()

        # 2️⃣ Sortowanie po dozwolonych polach
        allowed_fields = ['first_name', 'last_name', 'loyalty_points']
        if ordering:
            # dopuszczamy prefiks '-' dla malejącego sortowania
            field_name = ordering.lstrip('-')
            if field_name in allowed_fields:
                customers = customers.order_by(ordering)

        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def customer_detail_api(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return Response(
            {"error": f"Klient o id '{customer_id}' nie znaleziony"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def order_list_api(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            output_serializer = OrderSerializer(order)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def order_detail_api(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"error": f"Zamówienie o id {order_id} nie znalezione"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)