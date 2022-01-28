liczby = [2, 10, 12, 15, 20, 25, 30, 35] #tworzymy listę

#mapy - modyfikują argumenty w liście

def funkcja(x): #tworzymy funkcję z jednym argumentem
    return x * 2  #chcemy aby każdy argument był mnozony przez 2

wynik = map(funkcja, liczby) #zwiekszy każdą z naszych liczb * 2
print(list(wynik)) #konwertujemy postac mapy na listę

wynik2 = map(lambda x: x + 2, liczby) #taka sama funkcja jak u góry tylko z użyciem lambdy
print(list(wynik2))


#Filtry - nie modyfikuje liczb tylk daje nam true albo false

wynik3 = filter(lambda x: x % 2 == 0 , liczby) #czy dana liczba jest parzysta i jesli jest to wyswietla dana liczbę, jesli nie to nie wyswietla
print(list(wynik3))

