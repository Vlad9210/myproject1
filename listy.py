zmienna = 1
zmienna2 = "ABC"

lista = [1, 2, "c", "d", "e"]
print(lista)

print(lista[0]) #wywołanie z listy pierwszego elementu, zaczyna się od 0
print(lista[4])

lista[2] = 3 #zmiana jednego indeksu z listy
print(lista)

tekst = "Hello World"
print(tekst[0]) 

print(lista + ["f", "g"]) #przypisywanie kolejnych indeksów do listy

print(lista * 3) #mnożenie listy

print("Ilość elementów: ", len(lista)) #"len" - sprawdzanie długości listy

lista.append("f") #append - dołącza do listy kolejny element
print(lista)

lista.append(["g", "h"]) # w naiwasach [] dodaje kolejną listę
print(lista)
print(lista[6][0]) #wywołanie z listy "g" (6 element listy, 1 litera)

lista.insert(3, 3) #na pozycji 3 dodajemy kolejny element 3
print(lista)

print("Ilość: ", lista.count(3)) #count - wylicza ilość konkretnego elementu

print("Index: ", lista.index("f")) # index - sprawdzanie jaka w kolejnosci jest np. "F"
lista.remove("f") #remove - usuwa z listy
print(lista)

lista2 = [1, 20, 35, -5, 0]
print("Min: ", min(lista2)) #wyszukanie najmniejszej liczby z listy

lista2.sort() # sort - posortowanie listy od najmniejszego do największego
print(lista2)

lista2.reverse() #reverse - odwrócenie listy
print(lista2)

lista2.clear() #clear czyści listę od wszystkich elementów
print(lista2)
