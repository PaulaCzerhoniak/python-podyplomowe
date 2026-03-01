import os
import json
from django.core.management.base import BaseCommand
from menu_app.models import Pizza
from customers_app.models import Customer
from rozwiazanie_weekend2 import DATA_DIR


class Command(BaseCommand):
    help = 'Importuje dane z plikow JSON (rozwiazanie_weekend2) do bazy danych'

    def handle(self, *args, **options):
        self.import_pizzas()
        self.import_customers()

    def import_pizzas(self):
        menu_file = os.path.join(DATA_DIR, 'menu.json')
        try:
            with open(menu_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.WARNING(f"Plik {menu_file} nie istnieje"))
            return

        created = 0
        for item in data:
            pizza, was_created = Pizza.objects.get_or_create(
                name=item['name'],
                defaults={'price': item['price']}
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Pizze: zaimportowano {created}, juz istnialo {len(data) - created}"))

    def import_customers(self):
        customers_file = os.path.join(DATA_DIR, 'customers.json')
        try:
            with open(customers_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.WARNING(f"Plik {customers_file} nie istnieje"))
            return

        created = 0
        for item in data:
            # rozdzielamy pełne imię i nazwisko
            name_parts = item['name'].split(maxsplit=1)
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''

            customer_type = 'vip' if item.get('type') == 'VIPCustomer' else 'regular'
            customer, was_created = Customer.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                defaults={
                    'phone': item['phone'],
                    'customer_type': customer_type,
                    'discount_percent': item.get('discount_percent', 0),
                    'loyalty_points': item.get('loyalty_points', 0),
                }
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Klienci: zaimportowano {created}, juz istnialo {len(data) - created}"))