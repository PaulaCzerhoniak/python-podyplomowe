from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizza_list, name='pizza_list'),
    path('dodaj/', views.pizza_add, name='pizza_add'),
    path('<int:id>/edytuj/', views.pizza_edit, name='pizza_edit'),
    path('<int:id>/', views.pizza_detail, name='pizza_detail'),
    path('<int:id>/usun/', views.pizza_delete, name='pizza_delete'),  # <-- nowy URL
]