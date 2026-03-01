import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.urls import reverse
from .models import Pizza
# from rozwiazanie_weekend2 import DATA_DIR
# from rozwiazanie_weekend2.pizza import Menu, Pizza
# from rozwiazanie_weekend2.exceptions import PizzaNotFoundError, InvalidPriceError, DuplicatePizzaError

# MENU_FILE = os.path.join(DATA_DIR, 'menu.json')

# def pizza_list(request):
#     menu = Menu()
#     menu.load_from_file(MENU_FILE)
#     return render(request, 'menu_app/pizza_list.html', {'pizzas': list(menu)})

def pizza_list(request):
    pizzas = Pizza.objects.all().order_by('price') 
    return render(request, 'menu_app/pizza_list.html', {'pizzas': pizzas})

# def pizza_detail(request, name):
#     menu = Menu()
#     menu.load_from_file(MENU_FILE)
#     try:
#         pizza = menu.find_pizza(name)
#     except PizzaNotFoundError:
#         raise Http404(f"Pizza '{name}' nie znaleziona")
#     return render(request, 'menu_app/pizza_detail.html', {'pizza': pizza})

def pizza_detail(request, id):
    pizza = get_object_or_404(Pizza, id=id)
    return render(request, 'menu_app/pizza_detail.html', {'pizza': pizza})

# def pizza_add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '').strip()
#         price_str = request.POST.get('price', '').strip()

#         errors = []
#         if not name:
#             errors.append("Nazwa pizzy jest wymagana.")
#         if not price_str:
#             errors.append("Cena jest wymagana.")

#         if not errors:
#             try:
#                 price = float(price_str)
#                 pizza = Pizza(name, price)
#                 menu = Menu()
#                 menu.load_from_file(MENU_FILE)
#                 menu.add_pizza(pizza)
#                 menu.save_to_file(MENU_FILE)
#                 messages.success(request, f"Dodano pizzę: {name}")
#                 return redirect('pizza_list')
#             except (ValueError, TypeError) as e:
#                 errors.append(str(e))
#             except InvalidPriceError as e:
#                 errors.append(str(e))
#             except DuplicatePizzaError as e:
#                 errors.append(str(e))
                
#         for error in errors:
#             messages.error(request, error)

#         return render(request, 'menu_app/pizza_form.html', {
#             'name': name,
#             'price': price_str,
#         })

#     return render(request, 'menu_app/pizza_form.html')

def pizza_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        price_str = request.POST.get('price', '').strip()

        errors = []
        if not name:
            errors.append("Nazwa pizzy jest wymagana.")
        if not price_str:
            errors.append("Cena jest wymagana.")

        if not errors:
            try:
                price = float(price_str)
                Pizza.objects.create(name=name, price=price)
                messages.success(request, f"Dodano pizzę: {name}")
                return redirect('pizza_list')
            except (ValueError, TypeError):
                errors.append("Nieprawidlowa cena.")
            except ValidationError as e:
                errors.extend(e.messages)
            except IntegrityError:
                errors.append(f"Pizza '{name}' juz istnieje!")

        return render(request, 'menu_app/pizza_form.html', {
            'errors': errors,
            'name': name,
            'price': price_str,
        })

    return render(request, 'menu_app/pizza_form.html')

def pizza_edit(request, id):
    pizza = get_object_or_404(Pizza, id=id)

    if request.method == 'POST':
        new_name = request.POST.get('name', '').strip()
        price_str = request.POST.get('price', '').strip()

        errors = []
        if not new_name:
            errors.append("Nazwa pizzy jest wymagana.")
        if not price_str:
            errors.append("Cena jest wymagana.")

        if not errors:
            try:
                price = float(price_str)
                
                if pizza.name != new_name and Pizza.objects.filter(name=new_name).exists():
                    errors.append(f"Pizza '{new_name}' już istnieje!")
                else:
                    pizza.name = new_name
                    pizza.price = price
                    pizza.save()
                    messages.success(request, f"Zaktualizowano pizzę: {new_name}")
                    return redirect('pizza_list')
            except (ValueError, TypeError):
                errors.append("Nieprawidłowa cena.")
            except ValidationError as e:
                errors.extend(e.messages)
            except IntegrityError:
                errors.append(f"Pizza '{new_name}' już istnieje!")

        return render(request, 'menu_app/pizza_form.html', {
            'errors': errors,
            'name': new_name,
            'price': price_str,
            'pizza': pizza,
        })

    return render(request, 'menu_app/pizza_form.html', {
        'name': pizza.name,
        'price': pizza.price,
        'pizza': pizza,
    })
    
def pizza_delete(request, id):
    pizza = get_object_or_404(Pizza, id=id)
    if request.method == 'POST':
        pizza.delete()
        return redirect('pizza_list')  
    return redirect('pizza_detail', id=pizza.id)