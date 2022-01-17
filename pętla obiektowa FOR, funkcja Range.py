lista = ["Subskrybuj", "Kanat", "O", "Wszystkim"]

print(len(lista)) #długość listy

i = 0
while i < len(lista): #pętla While do wyswietlenie całej listy
    print(lista[i])
    i += 1

for x in lista : # pętla FOR - rób przez x w powyższej liście ( ta sama funkcja/rola co w powyzszej pętli While)
    print(x)

print(list(range(10))) # funkcja Range podaje listę od 0 do podanej liczby -1

for y in range(10): #wydrukuje od 0 do 9
    print(y)

for y in range(1, 11): #wydrukuje od 0 do 10
    print(y)

for y in range(1, 11, 2): #wydrukuje co drugą kwotę 
    print(y)

for y in range(0, 20, 3): #wydrukuje co 3 liczbę od 0
    print(y)