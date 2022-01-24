slownik = {1: "Poniedziałek", 2: "Wtorek", 7: "Niedziela"} #słownik posiada pary (klucz i wartośc )
print(slownik[1])
print(slownik[7])
slownik[3] = "Środa"
slownik[4] = False #możemy stosowac mix danych
slownik[5] = 5
print(slownik)
slownik["a"] = 1
print(slownik["a"])
print(slownik)

#print(slownik[8])
#print(slownik.get(8, "Inny dzień")

print("\nPętla:")
for l in slownik.values(): #values - wartości
    print(l)

print("\n------") #odstęp
print(slownik.pop(1)) # pop - usuwamy indeks
print(slownik)