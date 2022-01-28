liczby1 = {0, 1, 2, 4}
slowa = set(["a", "b", "c"])

print(liczby1)
print(slowa)

liczby1.add(5) #add - dodalismy do liczby1 kolejna liczbę
print(liczby1)
liczby1.remove(0) #usuwamy ze zbioru 0
print(liczby1)

liczby1.add(5) # przy kolejnym add 5 nie doda bo już jest jedna 5
print(liczby1)
#w "set" wartości sa unikalne, nie powtarzają się

print(1 in liczby1)
print("a" in liczby1)
#######
liczby1 = {0, 1, 2, 4}
liczby2 = {3, 4, 5, 6}

print(liczby1 | liczby2) # pozioma kreska "|"" to lub, jesli liczba jest w jednym lub drugim to połacz te zbiory
print(liczby1 & liczby2) # "&"" to część wspólna, liczby co sa w jednym i drugim zbiorze
print(liczby1 - liczby2) #perator róznicy, odejmowania "-"
print(liczby1 ^ liczby2) #operator "^" róznica symetryczna, wyświetla liczby z dwóch zbiorów ale bez liczb co sie powtarzają w tych zbiorach