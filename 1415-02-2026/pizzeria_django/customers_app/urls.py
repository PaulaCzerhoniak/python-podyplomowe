from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('dodaj/', views.customer_add, name='customer_add'),
    path('<int:id>/edytuj/', views.customer_edit, name='customer_edit'),
    path('<int:id>/usun/', views.customer_delete, name='customer_delete'),
]