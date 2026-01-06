import menu

menu.add_pizza("Margherita", 25)
menu.add_pizza("Pepperoni", 30)
menu.list_menu()

pizza = menu.find_pizza('Margherita')
print(f"Znaleziono: {pizza}")

pizza2 = menu.find_pizza('Funghi')
print(f"Znaleziono: {pizza2}")
