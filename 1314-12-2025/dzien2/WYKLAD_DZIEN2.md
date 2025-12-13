# Wykład: Programowanie obiektowe w Pythonie - Dzień 2

## Część 1: Wprowadzenie do programowania obiektowego

### Teoria: Podstawowe koncepcje OOP

Programowanie obiektowe (OOP) to paradygmat, w którym programy są zorganizowane wokół obiektów, łączących dane (atrybuty) i zachowania (metody). Pozwala na modelowanie świata rzeczywistego w kodzie.

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
- `margherita`, `pepperoni` - obiekty (instancje klasy)

#### Enkapsulacja (Encapsulation)

Enkapsulacja to mechanizm ukrywania wewnętrznej implementacji obiektu i wystawiania tylko niezbędnego interfejsu publicznego.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # prywatny atrybut (__)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Kwota musi być dodatnia")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Niewystarczające środki")

    def get_balance(self):
        return self.__balance

# Użycie
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # 1300
# print(account.__balance)  # AttributeError - prywatny!
```

**Zalety enkapsulacji:**
- Ochrona danych przed nieautoryzowanym dostępem
- Możliwość zmiany implementacji bez wpływu na kod używający klasy
- Lepsza kontrola nad modyfikacją danych

#### Metody specjalne (Magic Methods)

Python definiuje specjalne metody, które pozwalają klasom zachowywać się jak wbudowane typy:

```python
class Pizza:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        """Reprezentacja tekstowa dla użytkownika"""
        return f"{self.__name}: {self.__price} zł"

    def __repr__(self):
        """Reprezentacja dla developera"""
        return f"Pizza('{self.__name}', {self.__price})"

    def __eq__(self, other):
        """Porównanie równości"""
        if not isinstance(other, Pizza):
            return False
        return self.__name == other.name and self.__price == other.price

    @property
    def name(self):
        """Getter dla nazwy"""
        return self.__name

    @property
    def price(self):
        """Getter dla ceny"""
        return self.__price
```

**Najważniejsze metody specjalne:**
- `__init__()` - konstruktor
- `__str__()` - reprezentacja tekstowa (str(), print())
- `__repr__()` - reprezentacja dla debugowania
- `__eq__()` - porównanie równości (==)
- `__len__()` - długość obiektu (len())
- `__iter__()` - iteracja po obiekcie

**Dekoratory @property:**
- Umożliwiają dostęp do prywatnych atrybutów w kontrolowany sposób
- Składnia jak do atrybutu, ale wykonuje metodę

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

def list_pizzas():
    for pizza in pizzas:
        print(f"{pizza['name']}: {pizza['price']} zł")
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

    def __str__(self):
        return f"{self.__name}: {self.__price} zł"

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

    def list_pizzas(self):
        if not self.__pizzas:
            print("Menu puste!")
            return

        print("\n=== MENU ===")
        for pizza in self.__pizzas:
            print(f"  {pizza}")
```

**Zalety OOP:**
- Enkapsulacja - dane chronione, dostęp kontrolowany
- Walidacja w konstruktorze
- Dane i metody razem w jednej klasie
- Łatwiejsze testowanie i utrzymanie
- Możliwość rozszerzania przez dziedziczenie

---

## Część 3: Dziedziczenie (Inheritance)

### Teoria

Dziedziczenie pozwala na tworzenie nowych klas (podklas) na podstawie istniejących klas (klas bazowych), dziedziczących ich atrybuty i metody.

```python
class Customer:
    _next_id = 1  # Zmienna klasowa

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
        base = super().__str__()
        return f"{base} [VIP {self.__discount_percent}%, Punkty: {self.__loyalty_points}]"
```

**Kluczowe elementy:**
- `class VIPCustomer(Customer):` - VIPCustomer dziedziczy po Customer
- `super().__init__(...)` - wywołanie konstruktora klasy bazowej
- `super().__str__()` - wywołanie metody klasy bazowej
- Podklasa dziedziczy wszystkie metody i atrybuty rodzica
- Podklasa może dodawać nowe metody i atrybuty
- Podklasa może nadpisywać (override) metody rodzica

**Zalety dziedziczenia:**
- Ponowne użycie kodu (DRY - Don't Repeat Yourself)
- Hierarchiczna organizacja klas
- Łatwiejsze utrzymanie i rozszerzanie
- Modelowanie relacji "jest" (is-a relationship)

### Przykład: Hierarchia zwierząt

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Podklasy muszą implementować speak()")

class Dog(Animal):
    def speak(self):
        return f"{self.name} mówi: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} mówi: Meow!"

# Użycie
dog = Dog("Burek")
cat = Cat("Mruczek")

print(dog.speak())  # Burek mówi: Woof!
print(cat.speak())  # Mruczek mówi: Meow!
```

---

## Część 4: Polimorfizm (Polymorphism)

### Teoria

Polimorfizm pozwala na traktowanie obiektów różnych klas w jednolity sposób, jeśli implementują one te same metody.

```python
class Shape:
    def area(self):
        raise NotImplementedError("Podklasy muszą implementować area()")

    def perimeter(self):
        raise NotImplementedError("Podklasy muszą implementować perimeter()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Funkcja wykorzystująca polimorfizm
def print_shape_info(shape):
    print(f"Typ: {type(shape).__name__}")
    print(f"Pole: {shape.area():.2f}")
    print(f"Obwód: {shape.perimeter():.2f}")
    print("---")

# Użycie - różne typy, ten sam interfejs
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print_shape_info(shape)
```

**Duck typing w Pythonie:**

"If it walks like a duck and quacks like a duck, it's a duck"

```python
def make_sound(animal):
    # Nie sprawdzamy typu, tylko czy obiekt ma metodę speak
    return animal.speak()

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop!"

# Wszystkie działają, mimo że nie dziedziczą po wspólnej klasie
for obj in [Dog(), Cat(), Robot()]:
    print(make_sound(obj))
```

**Zalety polimorfizmu:**
- Elastyczność kodu
- Łatwiejsze rozszerzanie
- Możliwość pisania generycznego kodu
- Zmniejszenie zależności między klasami

---

## Część 5: Obsługa wyjątków (Exceptions)

### Teoria

Wyjątki w Pythonie to mechanizm obsługi błędów w czasie wykonania programu. Pozwalają na eleganckie radzenie sobie z nieoczekiwanymi sytuacjami.

#### Podstawowa składnia

```python
try:
    # Kod, który może rzucić wyjątek
    result = risky_operation()
except ValueError as e:
    print(f"Błąd wartości: {e}")
except ZeroDivisionError as e:
    print(f"Dzielenie przez zero: {e}")
except Exception as e:
    print(f"Ogólny błąd: {e}")
else:
    # Wykonane tylko jeśli nie było wyjątku
    print("Operacja zakończona sukcesem")
finally:
    # Wykonane zawsze (nawet jeśli był wyjątek)
    cleanup()
```

#### Rzucanie wyjątków

```python
class Pizza:
    def __init__(self, name, price):
        if not name:
            raise ValueError("Nazwa pizzy nie może być pusta")
        if price <= 0:
            raise ValueError("Cena musi być większa od zera")

        self.__name = name
        self.__price = price

# Użycie
try:
    pizza = Pizza("", 25.0)
except ValueError as e:
    print(f"Błąd: {e}")  # Błąd: Nazwa pizzy nie może być pusta
```

#### Własne wyjątki

```python
class PizzeriaError(Exception):
    """Bazowy wyjątek dla aplikacji pizzerii"""
    pass

class PizzaNotFoundError(PizzeriaError):
    """Pizza nie została znaleziona w menu"""
    pass

class CustomerNotFoundError(PizzeriaError):
    """Klient nie został znaleziony"""
    pass

class InvalidOrderError(PizzeriaError):
    """Zamówienie jest nieprawidłowe"""
    pass

# Użycie w klasie Menu
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

**Zalety własnych wyjątków:**
- Precyzyjne określenie typu błędu
- Łatwiejsze łapanie specyficznych błędów
- Lepsza dokumentacja kodu
- Możliwość hierarchii wyjątków

#### Best practices

```python
# ✅ DOBRZE: Konkretne wyjątki
try:
    value = int(user_input)
except ValueError:
    print("Nieprawidłowa liczba")

# ❌ ŹLE: Łapanie wszystkiego
try:
    value = int(user_input)
except:  # Nie rób tego!
    print("Coś poszło nie tak")

# ✅ DOBRZE: Rzucaj wcześnie
def process_order(order_id):
    if order_id is None:
        raise ValueError("order_id nie może być None")
    # ... dalszy kod

# ✅ DOBRZE: Finally do czyszczenia zasobów
file = None
try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("Plik nie istnieje")
finally:
    if file:
        file.close()
```

---

## Część 6: Operacje wejścia/wyjścia (I/O)

### Teoria

Operacje I/O pozwalają na zapisywanie i odczytywanie danych z plików, co umożliwia trwałe przechowywanie danych aplikacji.

#### Podstawowe operacje na plikach

```python
# Zapisywanie do pliku tekstowego
with open('menu.txt', 'w', encoding='utf-8') as f:
    f.write("Margherita: 25 zł\n")
    f.write("Pepperoni: 30 zł\n")

# Odczyt z pliku tekstowego
with open('menu.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# Odczyt linijka po linijce
with open('menu.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
```

**Context manager `with`:**
- Automatycznie zamyka plik
- Gwarantuje zwolnienie zasobów nawet w przypadku błędów
- Zalecana praktyka dla wszystkich operacji I/O

#### Praca z JSON

JSON (JavaScript Object Notation) to popularny format do serializacji danych.

```python
import json

# Zapis do JSON
menu_data = [
    {"name": "Margherita", "price": 25.0},
    {"name": "Pepperoni", "price": 30.0},
    {"name": "Hawajska", "price": 32.0}
]

with open('menu.json', 'w', encoding='utf-8') as f:
    json.dump(menu_data, f, indent=2, ensure_ascii=False)

# Odczyt z JSON
with open('menu.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    print(loaded_data)
```

#### Serializacja obiektów

```python
class Pizza:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

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
    def __init__(self):
        self.__pizzas = []

    def save_to_file(self, filename):
        """Zapisuje menu do pliku JSON"""
        data = [pizza.to_dict() for pizza in self.__pizzas]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_from_file(self, filename):
        """Wczytuje menu z pliku JSON"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.__pizzas = [Pizza.from_dict(item) for item in data]
            print(f"Wczytano {len(self.__pizzas)} pizz z pliku")

        except FileNotFoundError:
            print(f"Plik {filename} nie istnieje")
        except json.JSONDecodeError:
            print(f"Błąd parsowania JSON w pliku {filename}")

# Użycie
menu = Menu()
menu.add_pizza(Pizza("Margherita", 25.0))
menu.add_pizza(Pizza("Pepperoni", 30.0))

# Zapis
menu.save_to_file('menu.json')

# Odczyt
new_menu = Menu()
new_menu.load_from_file('menu.json')
```

**Zalety serializacji:**
- Trwałe przechowywanie danych
- Łatwa wymiana danych między programami
- Możliwość backupu i przywracania stanu aplikacji

---

## Część 7: Testowanie oprogramowania (Unit Testing)

### Teoria

Testowanie jednostkowe (unit testing) to praktyka weryfikacji poprawności poszczególnych jednostek kodu (funkcji, metod, klas) w izolacji.

#### Framework pytest

```bash
# Instalacja
pip install pytest

# Uruchomienie testów
pytest test_pizza.py -v
```

#### Podstawowe testy

```python
# test_pizza.py
import pytest
from pizza import Pizza, Menu

def test_pizza_creation():
    """Test tworzenia pizzy z poprawnymi danymi"""
    pizza = Pizza("Margherita", 25.0)
    assert pizza.name == "Margherita"
    assert pizza.price == 25.0

def test_pizza_invalid_price():
    """Test tworzenia pizzy z nieprawidłową ceną"""
    with pytest.raises(ValueError):
        Pizza("Test", -5)

def test_pizza_empty_name():
    """Test tworzenia pizzy z pustą nazwą"""
    with pytest.raises(ValueError):
        Pizza("", 25.0)

def test_pizza_str():
    """Test reprezentacji tekstowej pizzy"""
    pizza = Pizza("Pepperoni", 30.0)
    assert str(pizza) == "Pepperoni: 30.0 zł"
```

#### Testowanie klas

```python
class TestMenu:
    """Grupa testów dla klasy Menu"""

    def test_menu_creation(self):
        """Test tworzenia pustego menu"""
        menu = Menu()
        assert len(menu) == 0

    def test_add_pizza(self):
        """Test dodawania pizzy do menu"""
        menu = Menu()
        pizza = Pizza("Margherita", 25.0)
        menu.add_pizza(pizza)
        assert len(menu) == 1

    def test_add_duplicate_pizza(self):
        """Test dodawania duplikatu pizzy"""
        menu = Menu()
        pizza1 = Pizza("Margherita", 25.0)
        pizza2 = Pizza("Margherita", 30.0)

        menu.add_pizza(pizza1)
        with pytest.raises(ValueError):
            menu.add_pizza(pizza2)

    def test_find_pizza(self):
        """Test wyszukiwania pizzy"""
        menu = Menu()
        pizza = Pizza("Pepperoni", 30.0)
        menu.add_pizza(pizza)

        found = menu.find_pizza("Pepperoni")
        assert found is not None
        assert found.name == "Pepperoni"

    def test_find_nonexistent_pizza(self):
        """Test wyszukiwania nieistniejącej pizzy"""
        menu = Menu()
        found = menu.find_pizza("Nieistniejąca")
        assert found is None
```

#### Fixtures

Fixtures to sposób na przygotowanie danych testowych, które są używane w wielu testach.

```python
import pytest
from pizza import Pizza, Menu

@pytest.fixture
def sample_pizzas():
    """Fixture dostarczający przykładowe pizze"""
    return [
        Pizza("Margherita", 25.0),
        Pizza("Pepperoni", 30.0),
        Pizza("Hawajska", 32.0)
    ]

@pytest.fixture
def menu_with_pizzas(sample_pizzas):
    """Fixture dostarczający menu z pizzami"""
    menu = Menu()
    for pizza in sample_pizzas:
        menu.add_pizza(pizza)
    return menu

def test_menu_length(menu_with_pizzas):
    """Test używający fixture"""
    assert len(menu_with_pizzas) == 3

def test_cheapest_pizza(menu_with_pizzas):
    """Test znajdowania najtańszej pizzy"""
    cheapest = menu_with_pizzas.get_cheapest_pizza()
    assert cheapest.name == "Margherita"
    assert cheapest.price == 25.0
```

**Zalety testowania:**
- Wczesne wykrywanie błędów
- Dokumentacja oczekiwanego zachowania
- Ułatwienie refaktoryzacji (testy chronią przed regresją)
- Zwiększenie zaufania do kodu
- Wymuszenie lepszej architektury (testowalny kod to dobry kod)

#### Best practices

```python
# ✅ DOBRZE: Testy są niezależne
def test_add_pizza():
    menu = Menu()  # Każdy test tworzy własne obiekty
    pizza = Pizza("Test", 20.0)
    menu.add_pizza(pizza)
    assert len(menu) == 1

# ✅ DOBRZE: Jeden test = jedna rzecz
def test_pizza_name():
    pizza = Pizza("Margherita", 25.0)
    assert pizza.name == "Margherita"

def test_pizza_price():
    pizza = Pizza("Margherita", 25.0)
    assert pizza.price == 25.0

# ✅ DOBRZE: Nazwy testów opisują co testują
def test_adding_duplicate_pizza_raises_value_error():
    # Jasne co się testuje
    pass

# ❌ ŹLE: Niejasna nazwa
def test_pizza_2():
    pass
```

---

## Część 8: Refaktoryzacja aplikacji pizzerii

### Proces refaktoryzacji: Z proceduralnego na OOP

#### Krok 1: Identyfikacja obiektów

W aplikacji pizzerii możemy zidentyfikować następujące obiekty:
- **Pizza** - reprezentuje pojedynczą pizzę
- **Menu** - zarządza listą dostępnych pizz
- **Customer** - reprezentuje klienta
- **VIPCustomer** - specjalny typ klienta z rabatami
- **CustomerManager** - zarządza klientami
- **Order** - reprezentuje zamówienie
- **OrderItem** - pozycja w zamówieniu
- **OrderManager** - zarządza zamówieniami

#### Krok 2: Mapowanie odpowiedzialności

| Proceduralne (Dzień 1) | OOP (Dzień 2) |
|------------------------|---------------|
| `pizzas = []` (globalna lista) | `Menu.__pizzas` (prywatny atrybut) |
| `add_pizza(name, price)` | `Menu.add_pizza(Pizza)` |
| `find_pizza(name)` | `Menu.find_pizza(name)` |
| `customers = []` | `CustomerManager.__customers` |
| `add_customer(name, phone)` | `CustomerManager.add_customer(Customer)` |
| `orders = []` | `OrderManager.__orders` |
| `create_order(customer_id)` | `OrderManager.create_order(Customer)` |

#### Krok 3: Przykład refaktoryzacji

**PRZED (Proceduralne):**
```python
# menu.py
pizzas = []

def add_pizza(name, price):
    pizza = {'name': name, 'price': price}
    pizzas.append(pizza)
    print(f"Dodano: {name}")

def find_pizza(name):
    for pizza in pizzas:
        if pizza['name'] == name:
            return pizza
    return None

def list_pizzas():
    if not pizzas:
        print("Menu puste!")
        return

    print("\n=== MENU ===")
    for pizza in pizzas:
        print(f"  {pizza['name']}: {pizza['price']} zł")
```

**PO (OOP):**
```python
# pizza.py
class Pizza:
    """Reprezentuje pojedynczą pizzę z walidacją"""

    def __init__(self, name, price):
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

class Menu:
    """Zarządza kolekcją pizz"""

    def __init__(self):
        self.__pizzas = []

    def add_pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("Musi być typu Pizza")

        if any(p.name == pizza.name for p in self.__pizzas):
            raise ValueError(f"{pizza.name} już istnieje w menu")

        self.__pizzas.append(pizza)
        print(f"✓ Dodano: {pizza}")

    def find_pizza(self, name):
        for pizza in self.__pizzas:
            if pizza.name == name:
                return pizza
        return None

    def list_pizzas(self):
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
```

**Zalety po refaktoryzacji:**
- ✅ Walidacja danych w konstruktorze
- ✅ Enkapsulacja - dane chronione
- ✅ Sprawdzanie typów (isinstance)
- ✅ Metody specjalne (__len__, __iter__)
- ✅ Łatwiejsze testowanie
- ✅ Brak danych globalnych

#### Krok 4: Refaktoryzacja main.py

**PRZED:**
```python
from pizzeria import menu, customers, orders

menu.add_pizza("Margherita", 25.0)
cust1_id = customers.add_customer("Jan", "123")
order1_id = orders.create_order(cust1_id)
orders.add_item_to_order(order1_id, "Margherita", 2)
```

**PO:**
```python
from pizza import Pizza, Menu
from customer import Customer, CustomerManager
from order import Order, OrderManager

# Tworzenie managerów
menu = Menu()
customer_mgr = CustomerManager()
order_mgr = OrderManager(menu, customer_mgr)

# Dodawanie danych
pizza = Pizza("Margherita", 25.0)
menu.add_pizza(pizza)

customer = Customer("Jan", "123-456-789")
customer_mgr.add_customer(customer)

# Tworzenie zamówienia
order = order_mgr.create_order(customer)
order.add_item(pizza, 2)
print(order)
```

---

## Część 9: Zadania praktyczne i ćwiczenia

### Ćwiczenie 1: Podstawy OOP

1. **Klasa Pizza z walidacją** (15 min)
   - Zaimplementuj klasę Pizza z prywatnymi atrybutami
   - Dodaj walidację: nazwa niepusta, cena > 0
   - Zaimplementuj @property gettery
   - Dodaj metody __str__, __repr__, __eq__

2. **Klasa Menu** (20 min)
   - Zaimplementuj klasę Menu zarządzającą pizzami
   - Dodaj metody: add_pizza, find_pizza, list_pizzas
   - Sprawdź czy nie ma duplikatów
   - Zaimplementuj __len__ i __iter__

### Ćwiczenie 2: Dziedziczenie

1. **Hierarchia klientów** (25 min)
   - Klasa bazowa Customer
   - Klasa VIPCustomer z rabatem i punktami lojalnościowymi
   - Klasa CorporateCustomer z nazwą firmy
   - Test dziedziczenia: utwórz obiekty każdego typu

2. **CustomerManager** (20 min)
   - Klasa zarządzająca kolekcją klientów
   - Metody: add_customer, find_by_id, find_by_name
   - list_customers z sortowaniem

### Ćwiczenie 3: Wyjątki

1. **Własne wyjątki** (15 min)
   - PizzeriaError (bazowy)
   - PizzaNotFoundError
   - CustomerNotFoundError
   - InvalidOrderError

2. **Obsługa błędów** (20 min)
   - Dodaj obsługę wyjątków w Menu.find_pizza
   - Dodaj try-except w main.py
   - Test scenariuszy błędnych

### Ćwiczenie 4: I/O

1. **Serializacja Menu** (20 min)
   - Dodaj metodę save_to_file w Menu
   - Dodaj metodę load_from_file
   - Zaimplementuj to_dict i from_dict w Pizza

2. **Persistence całej aplikacji** (30 min)
   - Zapisz menu, klientów i zamówienia
   - Wczytaj i odtwórz stan aplikacji

### Ćwiczenie 5: Testy

1. **Testy jednostkowe Pizza** (20 min)
   - test_pizza_creation
   - test_invalid_price
   - test_invalid_name
   - test_pizza_equality

2. **Testy Menu** (25 min)
   - test_add_pizza
   - test_add_duplicate
   - test_find_pizza
   - test_menu_length

### Projekt końcowy: Pełna refaktoryzacja (60 min)

Przepisz całą aplikację z dnia 1 na OOP:

1. **Moduł pizza.py**
   - Klasy: Pizza, Menu
   - Walidacja, enkapsulacja
   - Własne wyjątki

2. **Moduł customer.py**
   - Klasy: Customer, VIPCustomer, CustomerManager
   - Dziedziczenie

3. **Moduł order.py**
   - Klasy: OrderItem, Order, OrderManager
   - Integracja z Menu i CustomerManager

4. **Moduł persistence.py**
   - Klasa DataManager
   - save_all(), load_all()

5. **Testy**
   - Co najmniej 10 testów pokrywających kluczowe funkcjonalności

6. **main.py**
   - Punkt wejścia
   - Interaktywne menu
   - Obsługa wyjątków

---

## Część 10: Podsumowanie

### Co osiągnęliśmy?

**Dzień 1 - Programowanie proceduralne:**
- ✅ Podstawy Python
- ✅ Funkcje i moduły
- ✅ Organizacja kodu w pakiety
- ✅ Działająca aplikacja pizzerii (proceduralna)

**Dzień 2 - Programowanie obiektowe:**
- ✅ Klasy i obiekty
- ✅ Enkapsulacja i ukrywanie danych
- ✅ Dziedziczenie i polimorfizm
- ✅ Własne wyjątki
- ✅ Operacje I/O (JSON)
- ✅ Testowanie (pytest)
- ✅ Refaktoryzacja: proceduralne → OOP

### Proceduralne vs OOP - Podsumowanie

| Aspekt | Proceduralne | OOP |
|--------|-------------|-----|
| **Organizacja** | Funkcje + dane globalne | Klasy (dane + metody) |
| **Enkapsulacja** | Brak | Prywatne atrybuty |
| **Walidacja** | Ręczna w każdej funkcji | W konstruktorze |
| **Rozszerzalność** | Trudna (copy-paste) | Łatwa (dziedziczenie) |
| **Testowanie** | Trudne (globalne dane) | Łatwe (izolowane obiekty) |
| **Utrzymanie** | Trudne w dużych projektach | Łatwiejsze |
| **Modelowanie** | Abstrakcyjne | Naturalne (rzeczywistość) |

### Kiedy używać OOP?

**OOP jest dobrym wyborem gdy:**
- Projekt jest średniej/dużej wielkości
- Modelujesz rzeczywiste obiekty
- Potrzebujesz enkapsulacji i walidacji
- Planujesz rozszerzanie funkcjonalności
- Pracujesz w zespole
- Chcesz łatwo testować kod

**Proceduralne może wystarczyć gdy:**
- Prosty skrypt (< 200 linii)
- Zadanie jednorazowe
- Brak potrzeby rozszerzania
- Proste przetwarzanie danych

### Co dalej?

**Tematy do zgłębienia:**
1. **Wzorce projektowe (Design Patterns)**
   - Singleton, Factory, Observer, Strategy

2. **Type hints**
   ```python
   def add_pizza(self, pizza: Pizza) -> None:
       ...
   ```

3. **Dataclasses** (Python 3.7+)
   ```python
   from dataclasses import dataclass

   @dataclass
   class Pizza:
       name: str
       price: float
   ```

4. **Programowanie asynchroniczne**
   - async/await
   - asyncio

5. **Zaawansowane testowanie**
   - Mocking
   - Coverage
   - TDD (Test-Driven Development)

### Zasoby do nauki

**Dokumentacja:**
- https://docs.python.org/3/ - Oficjalna dokumentacja Python
- https://docs.pytest.org/ - Dokumentacja pytest

**Kursy i tutoriale:**
- Real Python (https://realpython.com/)
- Python Tutor (http://pythontutor.com/) - wizualizacja kodu

**Książki:**
- "Fluent Python" - Luciano Ramalho
- "Python Tricks" - Dan Bader
- "Clean Code" - Robert C. Martin

---

## Gratulacje! 🎉

Ukończyłeś kurs programowania proceduralnego i obiektowego w Pythonie. Teraz potrafisz:
- Organizować kod w moduły i pakiety
- Pisać kod w stylu proceduralnym i obiektowym
- Używać enkapsulacji, dziedziczenia i polimorfizmu
- Obsługiwać wyjątki
- Zapisywać i wczytywać dane z plików
- Testować kod za pomocą pytest
- Refaktoryzować kod z proceduralnego na OOP

**Powodzenia w dalszej przygodzie z Pythonem!** 🐍
