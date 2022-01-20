def dzielenie(x, y):
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez o") # raise - wznieś, wyszucić wyjątek
    print(x / y)

try:
    dzielenie(2, 0)
except ZeroDivisionError:
    print("Błąd!")
    raise


def dzielenie(x, y):
    assert y != 0, "Y ==0" #assert - zapewnienie
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez o") # raise - wznieś, wyszucić wyjątek
    print(x / y)

try:
    dzielenie(2, 0)
except ZeroDivisionError:
    print("Błąd!")
    raise