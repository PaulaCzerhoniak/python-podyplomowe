from django.urls import path
from . import views

urlpatterns = [
    path('pizzas/', views.pizza_list_api, name='pizza_list_api'),
    path('pizzas/<str:name>/', views.pizza_detail_api, name='pizza_detail_api'),
    
    path('customers/', views.customer_list_api, name='customer_list_api'),
    path('customers/<int:customer_id>/', views.customer_detail_api, name='customer_detail_api'),
    
    path('orders/', views.order_list_api, name='order_list_api'),
    path('orders/<int:order_id>/', views.order_detail_api, name='order_detail_api'),
]