from rest_framework import serializers
from menu_app.models import Pizza
from customers_app.models import Customer
from orders_app.models import Order, OrderItem


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['name', 'price']
        
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'phone', 'customer_type', 'discount_percent', 'loyalty_points']
        read_only_fields = ['id', 'loyalty_points']
        
class OrderItemSerializer(serializers.ModelSerializer):
    pizza_name = serializers.CharField(source='pizza.name', read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['pizza_name', 'quantity', 'subtotal']

    def get_subtotal(self, obj):
        return obj.quantity * obj.pizza.price
         
class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'items', 'created_at', 'total_price']

    def get_customer_name(self, obj):
        return f"{obj.customer.first_name} {obj.customer.last_name}"

    def get_total_price(self, obj):
        return sum(item.quantity * item.pizza.price for item in obj.items.all())
    
class OrderCreateSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    items = serializers.ListField(
        child=serializers.DictField(child=serializers.IntegerField()),
        help_text="Lista słowników: {'pizza_id': int, 'quantity': int}"
    )

    def create(self, validated_data):
        from customers_app.models import Customer
        from menu_app.models import Pizza
        customer_id = validated_data['customer_id']
        items_data = validated_data['items']

        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Nie znaleziono klienta o podanym ID")

        order = Order.objects.create(customer=customer)

        for item in items_data:
            pizza_id = item.get('pizza_id')
            quantity = item.get('quantity', 1)
            try:
                pizza = Pizza.objects.get(id=pizza_id)
            except Pizza.DoesNotExist:
                raise serializers.ValidationError(f"Pizza o id {pizza_id} nie istnieje")
            OrderItem.objects.create(order=order, pizza=pizza, quantity=quantity)

        return order