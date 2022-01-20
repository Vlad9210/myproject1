x = 12
y = 0

# print(x / y) będzie błąd bo przez 0 nie można dzielić
try: # spróbuj wykonac operację
    print(x / y)
    print("Linijka po")
except ZeroDivisionError: #except - wyjątek
    print("Nastąpiło dzielenie przez 0!")

print("Dalsze instrukcje...")


x = 12
y = 2

try: # spróbuj wykonac operację
    print(x / y)
    print("Linijka po")
except ZeroDivisionError: #except - wyjątek
    print("Nastąpiło dzielenie przez 0!")

print("Dalsze instrukcje...")


x = 12
y = 2

try: # spróbuj wykonac operację
    print(x + "!") # suma int + str (nie może być i bedzie błąd)
    print(x / y)
    print("Linijka po")
except ZeroDivisionError: #except - wyjątek, można robic kilka wyjątków w jednej linijce - except(błąd1, błąd2)
    print("Nastąpiło dzielenie przez 0!")
except TypeError:
    print("Błąd typów danych.")
print("Dalsze instrukcje...")


x = 12
y = 2

try: # spróbuj wykonac operację
    print(x + "!") # suma int + str (nie może być i bedzie błąd)
    print(x / y)
    print("Linijka po")
except (ZeroDivisionError, TypeError): # można robic kilka wyjątków w jednej linijce - except(błąd1, błąd2)
    print("Wystąpił jeden zdwóch błędów")

print("Dalsze instrukcje...")


x = 12
y = 0

try: # spróbuj wykonac operację
    lista = [] #stworzenie pustej listy
    print(lista[0])
    print(x + "!") # suma int + str (nie może być i bedzie błąd)
    print(x / y)
    print("Linijka po")
except (ZeroDivisionError, TypeError): # można robic kilka wyjątków w jednej linijce - except(błąd1, błąd2)
    print("Wystąpił jeden zdwóch błędów")
except: #wyłapuje wszystkie inne błędy
    print("Inny błąd")
finally: #finally - zawsze sie wykona, bez wzgledu na błąd
    print("FINALLY wykonam się i tak")
print("Dalsze instrukcje...")


