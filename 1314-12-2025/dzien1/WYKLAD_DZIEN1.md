# Wykład: Programowanie proceduralne w Pythonie - Dzień 1

## Część 1: Wprowadzenie do programowania proceduralnego

### Teoria

Programowanie proceduralne to paradygmat programowania, w którym program jest podzielony na procedury lub funkcje, które operują na danych. Jest to jeden z najstarszych i najbardziej podstawowych podejść do programowania.

**Kluczowe cechy:**
- **Procedury/Funkcje**: Kod jest zorganizowany w funkcje, które wykonują określone zadania
- **Struktury danych**: Dane są przechowywane w zmiennych, listach, słownikach
- **Przepływ sterowania**: Używa się instrukcji warunkowych (if/elif/else), pętli (for/while)
- **Dane globalne**: Dane często przechowywane globalnie, dostępne dla wielu funkcji

**Zalety:**
- Proste i intuicyjne dla małych programów
- Łatwe do zrozumienia i debugowania
- Dobre dla zadań liniowych i proceduralnych

**Wady:**
- Trudności w zarządzaniu dużymi programami (duplikacja kodu, trudności w utrzymaniu)
- Brak enkapsulacji danych (dane są globalne lub przekazywane między funkcjami)
- Trudności w modelowaniu złożonych systemów rzeczywistych

**Przykład struktury proceduralnej:**
```python
# Dane globalne
menu_items = []

def add_menu_item(name, price):
    menu_items.append({'name': name, 'price': price})

def display_menu():
    for item in menu_items:
        print(f"{item['name']}: {item['price']} zł")
```

**Podkreśl:** Dane (lista `menu_items`) i funkcje są oddzielone!

---

## Część 2: Moduły i pakiety w Pythonie

### Teoria

Moduły w Pythonie to pliki `.py` zawierające definicje funkcji, klas, zmiennych. Pakiety to katalogi zawierające moduły i plik `__init__.py`, umożliwiające hierarchiczną organizację kodu.

**Tworzenie modułów:**
```python
# menu.py
def add_pizza(name, price):
    pass

def list_pizzas():
    pass
```

**Importowanie modułów:**
```python
import menu
from menu import add_pizza
import menu as m
```

**Tworzenie pakietów:**
```
pizzeria/
├── __init__.py
├── menu.py
├── orders.py
└── customers.py
```

**Korzyści z modułów i pakietów:**
- Ponowne użycie kodu
- Łatwiejsze zarządzanie projektem
- Izolacja funkcjonalności
- Lepsza czytelność kodu

---

## Część 3: Wprowadzenie do struktury projektu pizzerii

### Przegląd architektury

Dzisiaj zbudujemy system pizzerii składający się z trzech modułów:

**Struktura projektu:**
```
pizzeria/
├── __init__.py          # Marker pakietu
├── menu.py              # Zarządzanie menu
├── customers.py         # Zarządzanie klientami
├── orders.py            # Zarządzanie zamówieniami
└── main.py              # Punkt wejścia
```

**Moduł `menu.py`:**
- Przechowuje globalną listę pizz: `pizzas = []`
- Funkcje: `add_pizza()`, `list_pizzas()`, `find_pizza()`
- Każda pizza to słownik: `{'name': str, 'price': float}`

**Moduł `customers.py`:**
- Przechowuje listę klientów: `customers = []`
- Automatyczne generowanie ID: `next_customer_id = 1`
- Funkcje: `add_customer()`, `find_customer()`, `list_customers()`
- Struktura: `{'id': int, 'name': str, 'phone': str}`

**Moduł `orders.py`:**
- Integruje `menu` i `customers`
- Import: `from . import menu`
- Funkcje: `create_order()`, `add_item_to_order()`, `list_order()`
- Struktura: `{'id': int, 'customer_id': int, 'items': list}`

**Kluczowe obserwacje:**
- Dane globalne w każdym module
- Funkcje operują na globalnych danych
- `orders.py` importuje `menu.py` - zależność między modułami
- To jest **sedno programowania proceduralnego**

---

## Część 4: Live coding - Implementacja modułu `menu.py`

### Demonstracja (20 min live coding)

**Krok 1: Struktura pakietu**
```bash
mkdir pizzeria
touch pizzeria/__init__.py
```

**Krok 2: Implementacja `menu.py`**
```python
# Globalna lista pizz
pizzas = []

def add_pizza(name, price):
    """Dodaje pizzę do menu."""
    pizza = {'name': name, 'price': price}
    pizzas.append(pizza)
    print(f"✓ Dodano: {name} za {price} zł")

def list_pizzas():
    """Wyświetla wszystkie pizze."""
    if not pizzas:
        print("Menu jest puste!")
        return

    print("\n=== MENU ===")
    for pizza in pizzas:
        print(f"  {pizza['name']}: {pizza['price']} zł")

def find_pizza(name):
    """Znajduje pizzę po nazwie."""
    for pizza in pizzas:
        if pizza['name'] == name:
            return pizza
    return None
```

**Krok 3: Testowanie**
```python
# test_menu.py
from pizzeria import menu

menu.add_pizza("Margherita", 25.0)
menu.add_pizza("Pepperoni", 30.0)
menu.list_pizzas()

pizza = menu.find_pizza("Margherita")
print(f"\nZnaleziono: {pizza}")
```

### Ćwiczenie 1 (25 min)

**Zadanie:**
Zaimplementuj moduł `menu.py` jak pokazano powyżej, a następnie dodaj:

1. Funkcję `update_pizza_price(name, new_price)`:
   - Znajdź pizzę po nazwie (użyj `find_pizza`)
   - Zaktualizuj cenę
   - Wyświetl komunikat

2. Przetestuj w `test_menu.py`

**Bonus:**
- Walidacja: cena musi być > 0
- Funkcja `delete_pizza(name)`

---

## Część 5: Live coding - Implementacja modułu `customers.py`

### Demonstracja (20 min)

```python
# customers.py
customers = []
next_customer_id = 1

def add_customer(name, phone):
    """Dodaje nowego klienta."""
    global next_customer_id

    customer = {
        'id': next_customer_id,
        'name': name,
        'phone': phone
    }
    customers.append(customer)
    print(f"✓ Dodano klienta: {name} (ID: {next_customer_id})")

    next_customer_id += 1
    return customer['id']

def find_customer(customer_id):
    """Znajduje klienta po ID."""
    for customer in customers:
        if customer['id'] == customer_id:
            return customer
    return None

def list_customers():
    """Wyświetla wszystkich klientów."""
    if not customers:
        print("Brak klientów!")
        return

    print("\n=== KLIENCI ===")
    for customer in customers:
        print(f"  [{customer['id']}] {customer['name']} - {customer['phone']}")
```

**Podkreśl:**
- `global next_customer_id` - modyfikacja zmiennej globalnej
- Automatyczne generowanie ID
- Zwracanie ID umożliwia późniejsze odwołanie

### Ćwiczenie 2 (25 min)

**Zadanie:**
Zaimplementuj `customers.py` i dodaj:

1. Funkcję `update_customer_phone(customer_id, new_phone)`:
   - Znajdź klienta po ID
   - Zaktualizuj telefon
   - Wyświetl komunikat

2. Przetestuj pełny flow

**Bonus:**
- Walidacja telefonu (długość 9-12 znaków)
- Funkcja `find_customer_by_name(name)`

---

## Część 6: Live coding - Implementacja modułu `orders.py`

### Demonstracja (25 min)

**Kluczowe: Integracja z innymi modułami!**

```python
# orders.py
from pizzeria import menu  # ← Import innego modułu!

orders = []
next_order_id = 1

def create_order(customer_id):
    """Tworzy nowe zamówienie."""
    global next_order_id

    order = {
        'id': next_order_id,
        'customer_id': customer_id,
        'items': []
    }
    orders.append(order)
    print(f"✓ Utworzono zamówienie #{next_order_id}")

    next_order_id += 1
    return order['id']

def add_item_to_order(order_id, pizza_name, quantity):
    """Dodaje pozycję do zamówienia."""
    # 1. Znajdź zamówienie
    order = find_order(order_id)
    if not order:
        print(f"❌ Nie znaleziono zamówienia #{order_id}")
        return False

    # 2. Sprawdź czy pizza istnieje (integracja!)
    pizza = menu.find_pizza(pizza_name)
    if not pizza:
        print(f"❌ Nie znaleziono pizzy: {pizza_name}")
        return False

    # 3. Dodaj pozycję
    item = {
        'pizza_name': pizza_name,
        'price': pizza['price'],  # Snapshot ceny
        'quantity': quantity
    }
    order['items'].append(item)
    print(f"✓ Dodano {quantity}x {pizza_name}")
    return True

def find_order(order_id):
    """Znajduje zamówienie po ID."""
    for order in orders:
        if order['id'] == order_id:
            return order
    return None

def list_order(order_id):
    """Wyświetla szczegóły zamówienia."""
    order = find_order(order_id)
    if not order:
        print(f"❌ Nie znaleziono zamówienia #{order_id}")
        return

    print(f"\n=== ZAMÓWIENIE #{order_id} ===")
    print(f"Klient ID: {order['customer_id']}")
    print("Pozycje:")

    total = 0
    for item in order['items']:
        subtotal = item['price'] * item['quantity']
        total += subtotal
        print(f"  {item['quantity']}x {item['pizza_name']} = {subtotal} zł")

    print(f"RAZEM: {total} zł")
```

**Podkreśl:**
- Import `menu` - zależność między modułami
- Walidacja wielopoziomowa
- Snapshot ceny (dlaczego?)

### Ćwiczenie 3 (35 min)

**Zadanie:**
Zaimplementuj `orders.py` i dodaj:

1. Funkcję `remove_item_from_order(order_id, pizza_name)`:
   - Znajdź zamówienie
   - Usuń pozycję z daną pizzą
   - Wyświetl komunikat

2. Przetestuj pełny flow:
   - Dodaj pizze do menu
   - Dodaj klienta
   - Utwórz zamówienie
   - Dodaj 2-3 pozycje
   - Usuń jedną
   - Wyświetl zamówienie

**Bonus:**
- `cancel_order(order_id)` - usuwa całe zamówienie
- `list_all_orders()` - lista wszystkich zamówień

---

## Część 7: Integracja - plik `main.py`

### Demonstracja (10 min)

```python
# main.py
from pizzeria import menu, customers, orders

def main():
    print("=== APLIKACJA PIZZERII ===\n")

    # Menu
    menu.add_pizza("Margherita", 25.0)
    menu.add_pizza("Pepperoni", 30.0)
    menu.add_pizza("Hawajska", 32.0)
    menu.list_pizzas()

    # Klienci
    cust1_id = customers.add_customer("Jan Kowalski", "123-456-789")
    cust2_id = customers.add_customer("Anna Nowak", "987-654-321")
    customers.list_customers()

    # Zamówienie
    order1_id = orders.create_order(cust1_id)
    orders.add_item_to_order(order1_id, "Margherita", 2)
    orders.add_item_to_order(order1_id, "Pepperoni", 1)
    orders.list_order(order1_id)

if __name__ == "__main__":
    main()
```

**Wyjaśnij:**
- `if __name__ == "__main__":` - co to znaczy?
- Orkiestracja - `main.py` tylko wywołuje, nie zawiera logiki
- Typowy przepływ użycia systemu

### Ćwiczenie 4 (15 min)

**Zadanie:**
1. Stwórz `main.py` z pełną integracją
2. Dodaj drugie zamówienie dla drugiego klienta
3. Wyświetl oba zamówienia

**Bonus:**
Dodaj interaktywne menu (pętla `while` + `input`):
```
Menu:
1. Dodaj pizzę
2. Lista pizz
3. Nowe zamówienie
4. Koniec
```

---

## Część 8: Ćwiczenia zaawansowane

### Zadania do wyboru (40 min)

**A. Moduł inventory**
- Nowy moduł `inventory.py`
- Słownik składników: `{'sos': 100, 'ser': 50}`
- Funkcje: `add_ingredient()`, `use_ingredient()`, `check_availability()`
- Integracja z `orders.py` - sprawdzanie dostępności przy zamówieniu

**B. Walidacja danych**
- Dodaj walidację do wszystkich funkcji:
  - Cena > 0
  - Quantity > 0
  - Telefon: długość 9-12 znaków
- Zwracaj `False` lub rzucaj wyjątki przy błędnych danych

**C. Raportowanie**
- Funkcja `generate_daily_report()` w `orders.py`:
  - Liczba zamówień
  - Łączny przychód
  - Najpopularniejsza pizza (ile razy zamówiona)

---

## Część 9: Podsumowanie i analiza ograniczeń

### Co zbudowaliśmy?

✅ Działający system modułowy
✅ Trzy moduły: menu, customers, orders
✅ Integrację między modułami
✅ Podstawowe operacje CRUD

### Problemy podejścia proceduralnego

**1. Dane globalne**
```python
pizzas = []  # Każdy może to zmodyfikować!
menu.pizzas = []  # Wyczyszczenie całego menu
menu.pizzas.append({'name': 'Pizza', 'price': -100})  # Niespójna dana
```

**2. Brak enkapsulacji**
- Nie ma kontroli nad danymi
- Nie ma walidacji przy bezpośrednim dostępie
- Trudne debugowanie

**3. Brak związku między danymi i funkcjami**
```python
# Klient to tylko słownik:
customer = {'id': 1, 'name': 'Jan', 'phone': '123'}
# Gdzie jego metody? Gdzie zachowania?
```

**4. Trudność w rozszerzaniu**
- Dodanie nowej właściwości (np. kategoria pizzy) wymaga zmian w wielu miejscach
- Duplikacja logiki
- Rosnąca złożoność przy rozbudowie

**5. Problemy z testowaniem**
- Globalny stan trudny do resetowania
- Testy zależne od siebie
- Brak izolacji

### Pytania do przemyślenia

- Co jeśli dwa wątki jednocześnie dodają klienta? (race condition)
- Jak zabezpieczyć `pizzas` przed przypadkowym wyczyszczeniem?
- Jak dodać kategorię pizzy bez refaktoryzacji wszystkich funkcji?
- Jak testować funkcje które modyfikują stan globalny?

### Zapowiedź dnia 2

**Jutro zobaczymy** jak programowanie obiektowe rozwiązuje te problemy:

✅ **Enkapsulacja** - dane ukryte, dostęp tylko przez metody
✅ **Klasy** - połączenie danych i funkcji w jeden obiekt
✅ **Dziedziczenie** - rozszerzanie funkcjonalności bez duplikacji
✅ **Polimorfizm** - elastyczne zachowania obiektów

Przepiszemy dzisiejszą aplikację na styl obiektowy i zobaczymy różnicę!

---

## Materiały dodatkowe

### Struktura finalna projektu
```
pizzeria/
├── __init__.py
├── menu.py           # ✅ Zarządzanie menu
├── customers.py      # ✅ Zarządzanie klientami
├── orders.py         # ✅ Zarządzanie zamówieniami
└── main.py           # ✅ Integracja
```

### Przykład uruchomienia
```bash
cd pizzeria
python main.py
```

### Kluczowe koncepcje do zapamiętania

1. **Programowanie proceduralne** = funkcje + dane globalne
2. **Moduł** = plik `.py`
3. **Pakiet** = katalog z `__init__.py`
4. **Import** = `import nazwa` lub `from pakiet import modul`
5. **Dane globalne** = proste ale niebezpieczne
6. **Integracja modułów** = jeden moduł importuje drugi

---

**To koniec dnia 1!**

Jutro: **Programowanie obiektowe** - refaktoryzacja na klasy 🚀
