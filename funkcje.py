def funkcja_test():
    print("Funkcja...")

funkcja_test() # trzeba wywoływac funkcje, bez wywołania nic nie wyswietli

def dodaj(x):
    print(x + 1)

dodaj(2) #wyświetli na ekranie 3, czyli 2 + 1

def dodaj(x, y):
    print(x + y)

dodaj(2, 3) # sumuje x + y

def dodaj(x, y = 1): # ustawiamy domyślny paramentr y = y, po domyslnym parametrze nie można stawiać nie domyślnych, nie można wpisać np. z, domyslna zawsze na końcu!!!
    print(x + y)

dodaj(2)

def dodaj(x, y = 1, z = 0):
    print(x + y + z)

dodaj(2, 3, 5)

def dodaj(x, y = 1, z = 0):
    return x + y + z #return powinno być na końcu funkcji, po nim już nic nie będzie wyswietlane

dodaj(2, 3, 5)
