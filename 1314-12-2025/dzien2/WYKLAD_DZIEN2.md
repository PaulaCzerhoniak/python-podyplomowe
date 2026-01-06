# Wykład: Programowanie obiektowe w Pythonie - Dzień 2

## Agenda

**Czas trwania:** 8:30 - 15:00 (6h 30min z przerwami)

### Harmonogram

| Czas | Temat | Aktywność |
|------|-------|-----------|
| **8:30 - 8:50** | Powitanie i recap dnia 1 | Przypomnienie, Q&A |
| **8:50 - 9:30** | Teoria: Programowanie obiektowe | Wykład: OOP, enkapsulacja, metody specjalne |
| **9:30 - 10:30** | Porównanie: Proceduralne vs OOP | Analiza różnic + live demo |
| **10:30 - 10:40** | **PRZERWA** | 10 minut |
| **10:40 - 11:10** | Live coding: Klasa Pizza | Teoria → demo → ćwiczenie (15 min) |
| **11:10 - 11:45** | Live coding: Klasa Menu | Teoria → demo → ćwiczenie (20 min) |
| **11:45 - 12:40** | Live coding: Customer + dziedziczenie | Teoria → demo → ćwiczenie (25 min) |
| **12:40 - 13:10** | **PRZERWA** | 30 minut |
| **13:10 - 13:35** | Live coding: Własne wyjątki | Teoria → demo → ćwiczenie (15 min) |
| **13:35 - 14:05** | Live coding: I/O i JSON | Teoria → demo → ćwiczenie (20 min) |
| **14:05 - 14:35** | Live coding: Testy z pytest | Teoria → demo → ćwiczenie (20 min) |
| **14:35 - 14:50** | Projekt końcowy | Samodzielna refaktoryzacja proceduralne → OOP |
| **14:50 - 15:00** | Podsumowanie | Recap + Q&A |

### Co zbudujemy dzisiaj?

Przepisanie aplikacji pizzerii na **programowanie obiektowe**:
- **Klasy podstawowe** - Pizza, Menu, Customer
- **Dziedziczenie** - VIPCustomer
- **Refaktoryzacja** - pełne przepisanie z proceduralnego na OOP
- **Wyjątki** - własne klasy wyjątków
- **I/O** - zapis/odczyt danych do JSON
- **Testy** - unit testy z pytest

### Struktura projektu (OOP)

```
pizza_oop/
├── __init__.py
├── pizza.py         # klasy: Pizza, Menu
├── customer.py      # klasy: Customer, VIPCustomer
├── exceptions.py    # własne wyjątki
├── main.py          # punkt wejścia
└── test_pizza.py    # testy jednostkowe
```

### Czego się nauczysz?

- Klasy i obiekty w Pythonie
- Enkapsulacja i ukrywanie danych
- Dziedziczenie i polimorfizm
- Własne wyjątki
- Operacje I/O (JSON)
- Testowanie z pytest
- Refaktoryzacja: proceduralne → OOP

### Przygotowanie

Upewnij się, że masz:
- pytest zainstalowany: `pip install pytest`
- Kod z dnia 1 (dla porównania)
- Gotowość do refaktoryzacji!

---

## Część 1: Wprowadzenie do programowania obiektowego

### Teoria: Podstawowe koncepcje OOP

Programowanie obiektowe (OOP) to paradygmat, w którym programy są zorganizowane wokół obiektów, łączących dane (atrybuty) i zachowania (metody).

#### Klasy i obiekty

**Klasa** to szablon/przepis definiujący strukturę i zachowanie obiektów.
**Obiekt** to konkretna instancja klasy z własnymi wartościami atrybutów.

```python
class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} zł"

# Tworzenie obiektów (instancji)
margherita = Pizza("Margherita", 25.0)
pepperoni = Pizza("Pepperoni", 30.0)

print(margherita)  # Margherita: 25.0 zł
```

**Kluczowe elementy:**
- `class Pizza:` - definicja klasy (szablon)
- `__init__` - konstruktor, wywoływany przy tworzeniu obiektu
- `self` - referencja do bieżącego obiektu
- `margherita` - obiekt (instancja klasy)

#### Enkapsulacja (Encapsulation)

Enkapsulacja to ukrywanie wewnętrznej implementacji obiektu.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # prywatny atrybut (__)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)  # ERROR - prywatny!
```

**Zalety enkapsulacji:**
- Ochrona danych przed nieautoryzowanym dostępem
- Możliwość zmiany implementacji bez wpływu na kod
- Lepsza kontrola nad modyfikacją danych

#### Metody specjalne i @property

```python
class Pizza:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        """Getter dla nazwy"""
        return self.__name

    @property
    def price(self):
        """Getter dla ceny"""
        return self.__price

    def __str__(self):
        return f"{self.__name}: {self.__price} zł"

    def __repr__(self):
        return f"Pizza('{self.__name}', {self.__price})"
```

**Najważniejsze metody specjalne:**
- `__init__()` - konstruktor
- `__str__()` - reprezentacja tekstowa
- `__repr__()` - reprezentacja dla debugowania
- `__eq__()` - porównanie równości
- `__len__()` - długość obiektu

---

## Część 2: Porównanie: Proceduralne vs OOP

### Programowanie proceduralne (Dzień 1)

```python
# menu.py
pizzas = []  # Dane globalne

def add_pizza(name, price):
    pizza = {'name': name, 'price': price}
    pizzas.append(pizza)

def find_pizza(name):
    for pizza in pizzas:
        if pizza['name'] == name:
            return pizza
    return None
```

**Problemy:**
- Dane globalne - każdy może je modyfikować
- Brak związku między danymi i funkcjami
- Trudność w zarządzaniu przy dużych projektach
- Brak walidacji danych

### Programowanie obiektowe (Dzień 2)

```python
# pizza.py
class Pizza:
    def __init__(self, name, price):
        if price <= 0:
            raise ValueError("Cena musi być > 0")
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

class Menu:
    def __init__(self):
        self.__pizzas = []  # Dane prywatne

    def add_pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("Musi być typu Pizza")
        if any(p.name == pizza.name for p in self.__pizzas):
            raise ValueError(f"{pizza.name} już istnieje")
        self.__pizzas.append(pizza)

    def find_pizza(self, name):
        for pizza in self.__pizzas:
            if pizza.name == name:
                return pizza
        return None
```

**Zalety OOP:**
- Enkapsulacja - dane chronione
- Walidacja w konstruktorze
- Dane i metody razem
- Łatwiejsze testowanie
- Możliwość rozszerzania przez dziedziczenie

---

## Część 3: Live coding - Implementacja klasy `Pizza`

### Teoria: Budowa klasy z walidacją

Klasa Pizza powinna:
- Przechowywać nazwę i cenę jako prywatne atrybuty
- Walidować dane w konstruktorze
- Udostępniać gettery przez @property
- Implementować metody specjalne

### Przykład implementacji

```python
# pizza.py
class Pizza:
    """Reprezentuje pojedynczą pizzę z walidacją"""

    def __init__(self, name, price):
        """
        Tworzy nową pizzę.

        Args:
            name (str): Nazwa pizzy
            price (float): Cena pizzy

        Raises:
            ValueError: Jeśli nazwa pusta lub cena <= 0
        """
        if not name:
            raise ValueError("Nazwa nie może być pusta")
        if price <= 0:
            raise ValueError("Cena musi być > 0")

        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name}: {self.__price} zł"

    def __repr__(self):
        return f"Pizza('{self.__name}', {self.__price})"

    def __eq__(self, other):
        if not isinstance(other, Pizza):
            return False
        return self.name == other.name and self.price == other.price

# Przykład użycia
pizza1 = Pizza("Margherita", 25.0)
pizza2 = Pizza("Pepperoni", 30.0)

print(pizza1)  # Margherita: 25.0 zł
print(repr(pizza1))  # Pizza('Margherita', 25.0)
print(pizza1 == pizza2)  # False
```

### Ćwiczenie praktyczne

**Zadanie (15 min):**

Zaimplementuj klasę `Pizza` według powyższego wzoru i dodaj:

1. **Metodę `apply_discount(percent)`**
   - Zwraca nową cenę po rabacie
   - Przykład: `pizza.apply_discount(10)` → zwraca 22.5 dla pizzy za 25 zł

2. **Metodę `update_price(new_price)`**
   - Aktualizuje cenę pizzy
   - Walidacja: new_price > 0
   - Rzuca ValueError jeśli nieprawidłowa cena

3. **Przetestuj:**
   ```python
   pizza = Pizza("Margherita", 25.0)
   print(pizza)
   print(f"Po rabacie 10%: {pizza.apply_discount(10)} zł")
   pizza.update_price(28.0)
   print(pizza)
   ```

**Oczekiwany output:**
```
Margherita: 25.0 zł
Po rabacie 10%: 22.5 zł
Margherita: 28.0 zł
```

---

## Część 4: Live coding - Implementacja klasy `Menu`

### Teoria: Kolekcje obiektów

Klasa Menu zarządza kolekcją obiektów Pizza. Powinna:
- Przechowywać pizze w prywatnej liście
- Sprawdzać typy dodawanych obiektów
- Zapobiegać duplikatom
- Udostępniać metody __len__ i __iter__

### Przykład implementacji

```python
class Menu:
    """Zarządza kolekcją pizz"""

    def __init__(self):
        self.__pizzas = []

    def add_pizza(self, pizza):
        """Dodaje pizzę do menu"""
        if not isinstance(pizza, Pizza):
            raise TypeError("Musi być typu Pizza")

        if any(p.name == pizza.name for p in self.__pizzas):
            raise ValueError(f"{pizza.name} już istnieje w menu")

        self.__pizzas.append(pizza)
        print(f"Dodano: {pizza}")

    def find_pizza(self, name):
        """Znajduje pizzę po nazwie"""
        for pizza in self.__pizzas:
            if pizza.name == name:
                return pizza
        return None

    def remove_pizza(self, name):
        """Usuwa pizzę z menu"""
        pizza = self.find_pizza(name)
        if pizza:
            self.__pizzas.remove(pizza)
            print(f"Usunięto: {name}")
            return True
        return False

    def list_pizzas(self):
        """Wyświetla wszystkie pizze"""
        if not self.__pizzas:
            print("Menu jest puste!")
            return

        print("\n=== MENU ===")
        for pizza in self.__pizzas:
            print(f"  {pizza}")

    def __len__(self):
        return len(self.__pizzas)

    def __iter__(self):
        return iter(self.__pizzas)

# Przykład użycia
menu = Menu()
menu.add_pizza(Pizza("Margherita", 25.0))
menu.add_pizza(Pizza("Pepperoni", 30.0))
menu.add_pizza(Pizza("Hawajska", 32.0))

menu.list_pizzas()
print(f"Liczba pizz: {len(menu)}")

found = menu.find_pizza("Margherita")
print(f"Znaleziono: {found}")
```

### Ćwiczenie praktyczne

**Zadanie (20 min):**

Zaimplementuj klasę `Menu` i dodaj następujące metody:

1. **`get_cheapest_pizza()`**
   - Zwraca najtańszą pizzę z menu
   - Zwraca None jeśli menu puste

2. **`get_most_expensive_pizza()`**
   - Zwraca najdroższą pizzę

3. **`get_average_price()`**
   - Zwraca średnią cenę pizz w menu
   - Zwraca 0 jeśli menu puste

4. **Przetestuj:**
   ```python
   menu = Menu()
   menu.add_pizza(Pizza("Margherita", 25.0))
   menu.add_pizza(Pizza("Pepperoni", 30.0))
   menu.add_pizza(Pizza("Hawajska", 32.0))

   print(f"Najtańsza: {menu.get_cheapest_pizza()}")
   print(f"Najdroższa: {menu.get_most_expensive_pizza()}")
   print(f"Średnia cena: {menu.get_average_price():.2f} zł")
   ```

**Oczekiwany output:**
```
Najtańsza: Margherita: 25.0 zł
Najdroższa: Hawajska: 32.0 zł
Średnia cena: 29.00 zł
```

---

## Część 5: Live coding - Klasa `Customer` i dziedziczenie

### Teoria: Dziedziczenie w Pythonie

Dziedziczenie pozwala na tworzenie nowych klas na podstawie istniejących, dziedzicząc ich funkcjonalność.

**Kluczowe elementy:**
- `class Podklasa(KlasaBazowa):` - składnia dziedziczenia
- `super().__init__(...)` - wywołanie konstruktora rodzica
- Podklasa dziedziczy wszystkie metody rodzica
- Podklasa może dodawać nowe metody
- Podklasa może nadpisywać (override) metody rodzica

### Przykład implementacji

```python
class Customer:
    """Reprezentuje klienta pizzerii"""

    _next_id = 1  # Zmienna klasowa - współdzielona przez wszystkie instancje

    def __init__(self, name, phone):
        self.__id = Customer._next_id
        Customer._next_id += 1
        self.__name = name
        self.__phone = phone

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    def __str__(self):
        return f"[{self.__id}] {self.__name} - {self.__phone}"


class VIPCustomer(Customer):  # Dziedziczenie!
    """Klient VIP z rabatem i punktami lojalnościowymi"""

    def __init__(self, name, phone, discount_percent):
        super().__init__(name, phone)  # Konstruktor rodzica
        self.__discount_percent = discount_percent
        self.__loyalty_points = 0

    @property
    def discount_percent(self):
        return self.__discount_percent

    @property
    def loyalty_points(self):
        return self.__loyalty_points

    def apply_discount(self, price):
        """Stosuje rabat VIP do ceny"""
        return price * (1 - self.__discount_percent / 100)

    def add_loyalty_points(self, points):
        """Dodaje punkty lojalnościowe"""
        if points > 0:
            self.__loyalty_points += points

    def __str__(self):
        base = super().__str__()  # Wywołanie metody rodzica
        return f"{base} [VIP {self.__discount_percent}%, Punkty: {self.__loyalty_points}]"


# Przykład użycia
customer1 = Customer("Jan Kowalski", "123-456-789")
customer2 = VIPCustomer("Anna Nowak", "987-654-321", 15)

print(customer1)  # [1] Jan Kowalski - 123-456-789
print(customer2)  # [2] Anna Nowak - 987-654-321 [VIP 15%, Punkty: 0]

customer2.add_loyalty_points(50)
print(customer2)  # [2] Anna Nowak - 987-654-321 [VIP 15%, Punkty: 50]

price = 100.0
discounted = customer2.apply_discount(price)
print(f"Cena po rabacie VIP: {discounted} zł")  # 85.0 zł
```

### Ćwiczenie praktyczne

**Zadanie (25 min):**

Zaimplementuj klasy `Customer` i `VIPCustomer`, oraz dodaj:

1. **Klasę `CorporateCustomer(Customer)`**
   - Dziedziczy po Customer
   - Dodatkowy atrybut: `company_name`
   - Metoda `get_invoice_data()` - zwraca słownik z danymi do faktury

2. **Klasę `CustomerManager`**
   - Zarządza kolekcją klientów
   - Metody:
     - `add_customer(customer)` - dodaje klienta
     - `find_customer_by_id(id)` - znajduje klienta po ID
     - `list_customers()` - wyświetla wszystkich klientów

3. **Przetestuj:**
   ```python
   manager = CustomerManager()
   manager.add_customer(Customer("Jan", "123"))
   manager.add_customer(VIPCustomer("Anna", "456", 15))
   manager.add_customer(CorporateCustomer("Firma XYZ", "789", "XYZ Sp. z o.o."))

   manager.list_customers()
   ```

---

## Część 6: Live coding - Własne wyjątki

### Teoria: Hierarchia wyjątków

Własne wyjątki pozwalają na precyzyjne określenie typu błędu w aplikacji.

```python
class PizzeriaError(Exception):
    """Bazowy wyjątek dla aplikacji pizzerii"""
    pass

class PizzaNotFoundError(PizzeriaError):
    """Pizza nie została znaleziona"""
    pass

class CustomerNotFoundError(PizzeriaError):
    """Klient nie został znaleziony"""
    pass

# Użycie
class Menu:
    def find_pizza(self, name):
        for pizza in self.__pizzas:
            if pizza.name == name:
                return pizza
        raise PizzaNotFoundError(f"Nie znaleziono pizzy: {name}")

# Łapanie
try:
    pizza = menu.find_pizza("Nieistniejąca")
except PizzaNotFoundError as e:
    print(f"Błąd: {e}")
```

### Ćwiczenie praktyczne

**Zadanie (15 min):**

1. **Utwórz plik `exceptions.py`** z hierarchią wyjątków:
   - PizzeriaError (bazowy)
   - PizzaNotFoundError
   - CustomerNotFoundError
   - InvalidPriceError

2. **Dodaj obsługę wyjątków** do klas Menu i CustomerManager

3. **Przetestuj:**
   ```python
   try:
       menu.find_pizza("Nieistniejąca")
   except PizzaNotFoundError as e:
       print(f"Błąd: {e}")

   try:
       Pizza("Test", -5)
   except InvalidPriceError as e:
       print(f"Błąd: {e}")
   ```

---

## Część 7: Live coding - Zapis/odczyt danych (I/O)

### Teoria: Serializacja do JSON

```python
import json

class Pizza:
    def to_dict(self):
        """Konwersja do słownika (serializacja)"""
        return {
            'name': self.__name,
            'price': self.__price
        }

    @classmethod
    def from_dict(cls, data):
        """Tworzenie obiektu ze słownika (deserializacja)"""
        return cls(data['name'], data['price'])

class Menu:
    def save_to_file(self, filename):
        """Zapisuje menu do pliku JSON"""
        data = [pizza.to_dict() for pizza in self.__pizzas]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_from_file(self, filename):
        """Wczytuje menu z pliku JSON"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.__pizzas = [Pizza.from_dict(item) for item in data]
```

### Ćwiczenie praktyczne

**Zadanie (20 min):**

1. **Dodaj metody serializacji** do klas Pizza, Customer
2. **Dodaj metody save/load** do Menu i CustomerManager
3. **Przetestuj:**
   ```python
   menu = Menu()
   menu.add_pizza(Pizza("Margherita", 25.0))
   menu.save_to_file('menu.json')

   new_menu = Menu()
   new_menu.load_from_file('menu.json')
   new_menu.list_pizzas()
   ```

---

## Część 8: Live coding - Testy jednostkowe (pytest)

### Teoria: Testowanie z pytest

```python
# test_pizza.py
import pytest
from pizza import Pizza, Menu

def test_pizza_creation():
    pizza = Pizza("Margherita", 25.0)
    assert pizza.name == "Margherita"
    assert pizza.price == 25.0

def test_pizza_invalid_price():
    with pytest.raises(ValueError):
        Pizza("Test", -5)

def test_menu_add_pizza():
    menu = Menu()
    pizza = Pizza("Test", 20.0)
    menu.add_pizza(pizza)
    assert len(menu) == 1
```

### Ćwiczenie praktyczne

**Zadanie (20 min):**

Napisz testy dla:
1. Tworzenia pizzy (poprawne i niepoprawne dane)
2. Dodawania pizzy do menu
3. Wyszukiwania pizzy
4. Duplikatów w menu

Uruchom: `pytest test_pizza.py -v`

---

## Część 9: Projekt końcowy - Refaktoryzacja

### Zadanie: Przepisz aplikację z Dnia 1 na OOP

**Czas: 60 min**

Przepisz całą aplikację pizzerii z programowania proceduralnego na obiektowe:

1. **Moduł pizza.py**
   - Klasy: Pizza, Menu
   - Walidacja, enkapsulacja
   - Metody: to_dict, from_dict

2. **Moduł customer.py**
   - Klasy: Customer, VIPCustomer, CustomerManager

3. **Moduł exceptions.py**
   - Hierarchia wyjątków

4. **Moduł main.py**
   - Punkt wejścia aplikacji
   - Użycie wszystkich klas

5. **Testy**
   - test_pizza.py
   - test_customer.py

**Porównaj z wersją proceduralną - co się poprawiło?**

---

## Część 10: Podsumowanie

### Co osiągnęliśmy?

**Dzień 1:**
- Programowanie proceduralne
- Funkcje i moduły
- Aplikacja pizzerii (proceduralna)

**Dzień 2:**
- Klasy i obiekty
- Enkapsulacja
- Dziedziczenie
- Własne wyjątki
- I/O i serializacja
- Testy jednostkowe
- Refaktoryzacja: proceduralne → OOP

### Porównanie

| Aspekt | Proceduralne | OOP |
|--------|-------------|-----|
| **Organizacja** | Funkcje + dane globalne | Klasy (dane + metody) |
| **Enkapsulacja** | Brak | Prywatne atrybuty |
| **Walidacja** | Ręczna | W konstruktorze |
| **Rozszerzalność** | Trudna | Łatwa (dziedziczenie) |
| **Testowanie** | Trudne | Łatwe |

### Co dalej?

**Tematy do zgłębienia:**
1. Wzorce projektowe (Design Patterns)
2. Type hints
3. Dataclasses
4. Programowanie asynchroniczne
5. TDD (Test-Driven Development)

### Zasoby

- https://docs.python.org/3/
- https://realpython.com/
- "Fluent Python" - Luciano Ramalho
- "Clean Code" - Robert C. Martin

---

## Gratulacje!

Ukończyłeś kurs programowania proceduralnego i obiektowego w Pythonie!

Teraz potrafisz:
- Organizować kod w moduły i pakiety
- Pisać kod proceduralny i obiektowy
- Używać enkapsulacji, dziedziczenia
- Obsługiwać wyjątki
- Testować kod z pytest
- Refaktoryzować kod

**Powodzenia w dalszej przygodzie z Pythonem!**
