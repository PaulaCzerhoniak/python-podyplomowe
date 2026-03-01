import os
import re
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages 
# from rozwiazanie_weekend2 import DATA_DIR
# from rozwiazanie_weekend2.customer import Customer, VIPCustomer, CustomerManager
from .models import Customer
from .forms import CustomerForm

# CUSTOMERS_FILE = os.path.join(DATA_DIR, 'customers.json')

# def customer_list(request):
#     manager = CustomerManager()
#     manager.load_from_file(CUSTOMERS_FILE)
#     return render(request, 'customers_app/customer_list.html', {
#         'customers': list(manager),
#     })

def customer_list(request):
    sort = request.GET.get('sort', 'id')  # domyślnie sortuj po id
    allowed_sorts = ['id', '-id', 'first_name', '-first_name', 'last_name', '-last_name',
                     'customer_type', '-customer_type', 'loyalty_points', '-loyalty_points']

    if sort not in allowed_sorts:
        sort = 'id'

    customers = Customer.objects.all().order_by(sort)
    return render(request, 'customers_app/customer_list.html', {
        'customers': customers,
        'current_sort': sort
    })
    
# def customer_add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '').strip()
#         phone = request.POST.get('phone', '').strip()
#         customer_type = request.POST.get('type', 'regular')

#         errors = []
        
#         if not name:
#             errors.append("Imie klienta jest wymagane.")
#         if not phone:
#             errors.append("Numer telefonu jest wymagany.")
#         else:
#             if not re.match(r'^\d{3}-\d{3}-\d{3}$', phone):
#                 errors.append("Numer telefonu musi być w formacie XXX-XXX-XXX.")

#         if not errors:
#             try:
#                 manager = CustomerManager()
#                 manager.load_from_file(CUSTOMERS_FILE)

#                 if customer_type == 'vip':
#                     discount = float(request.POST.get('discount', 10))
#                     customer = VIPCustomer(name, phone, discount)
#                 else:
#                     customer = Customer(name, phone)

#                 manager.add_customer(customer)
#                 manager.save_to_file(CUSTOMERS_FILE)
#                 messages.success(request, f"Dodano klienta: {name}")
#                 return redirect('customer_list')
            
#             except Exception as e:
#                 errors.append(str(e))   
            
#         for error in errors:
#             messages.error(request, error)  

#         return render(request, 'customers_app/customer_form.html', {
#             'name': name,
#             'phone': phone,
#         })

#     return render(request, 'customers_app/customer_form.html')

def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers_app/customer_form.html', {'form': form})

def customer_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers_app/customer_form.html', {'form': form})

def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return redirect('customer_list')