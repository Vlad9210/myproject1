krotka = (2, 4, 8, 16, 32, 64, 128)
print(krotka[0])
print(krotka[6])
print(krotka)
#krotka[0] = 1 #nie możemy zmieniać wartości elementów , będzie błąd "tuple"False

print("Elementów:", krotka.count(2)) #count - ilość elementów
print("Index:", krotka.index(64)) # index - czyli sprawdza na której pozycji jest dany index


print("\nWycinki:") #\n - w nowej linii
print(krotka[0:3]) #tworzy nową krotkę od indeksa 0 do 3-1
print(krotka[3:5]) # będą indeksy 3 i 4
print(krotka[0:7])
print(krotka[-4:-2]) #bedą to wartości 16 i 32 bo przy - liczymy od końca
print(krotka[0:7:2]) # dodajemy 3 parament "element skoku" - bedzie wyswietlany co 2 element
print(krotka[:4]) # nie podając 1 paramentru będzie liczony od początku do 4-1 elementu
print(krotka[::-1]) # nie podajemy ani 1 ani 2 elementu i będzie to cała lista w odwrotnej kolejności


