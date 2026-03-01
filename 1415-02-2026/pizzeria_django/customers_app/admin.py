from django.contrib import admin   # <- to jest potrzebne!
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'customer_type', 'loyalty_points')
    list_filter = ['customer_type']
    search_fields = ['first_name', 'last_name', 'phone']