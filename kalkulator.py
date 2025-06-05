import logging

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Funkcje działań
def addition(a, b):
    if a > 0 and b > 0:
        logging.info(f"Dodaję {a} i {b}")
        return a + b
    return "Obie liczby muszą być większe od zera"

def subtraction(a, b):
    if a > 0 and b > 0:
        logging.info(f"Odejmuję {b} od {a}")
        return a - b
    return "Obie liczby muszą być większe od zera"

def multiplication(a, b):
    if a > 0 and b > 0:
        logging.info(f"Mnożę {a} i {b}")
        return a * b
    return "Obie liczby muszą być większe od zera"

def division(a, b):
    if a > 0 and b > 0:
        logging.info(f"Dzielę {a} przez {b}")
        return a / b
    return "Obie liczby muszą być większe od zera"

# Menu wyboru
print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1 Dodawanie")
print("2 Odejmowanie")
print("3 Mnożenie")
print("4 Dzielenie")

# Pobieranie typu działania
number = int(input(">> "))

# Pobieranie liczb
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

# Wykonanie działania
if number == 1:
    result = addition(a, b)
elif number == 2:
    result = subtraction(a, b)
elif number == 3:
    result = multiplication(a, b)
elif number == 4:
    result = division(a, b)
else:
    result = "Nieprawidłowy wybór działania."

# Wyświetlenie wyniku
print(f"Wynik to: {result}")