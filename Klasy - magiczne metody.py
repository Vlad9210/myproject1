import math

class Punkt2D: #bez nawiasów bo to by było dziedziczenie
# metoda "init" - zawsze wywoływana w momencie tworzenia obiektu na bazie danej klasy, czyli w momencie kiedy bierzemy klasę i przekształcamy ja w obiekt
    def __init__(self, x, y):   #metody magiczne rozpoczynają się i kończą podwójnym podkresleniem __
        self.x = x
        self.y = y
        self.odleglosc = math.sqrt(x**2 + y**2)  #tworzymy  dodatkową zmienna odległość

    def __add__(self, drugi): #metoda magiczna "add" - służy przy doawaniu
        return Punkt2D(self.x + drugi.x, self.y + drugi.y)

    def __lt__(self, drugi):  ##"lt" - metoda less than - mniejsze od
            return self.odleglosc < drugi.odleglosc

 # metoda "le" - less equal - mniejsze bądź równe
 #metoda "gt" - graither than - wieksze od
 # metoda "ge" - wieksze bądź równe
 # metoda "ne" - not equal - nie równe
 # metoda "eq" - equal - równe
    def ___eq__(self, drugi):
        return self.x == drugi.x and self.y == drugi.y

    def __len__(self):
        return int(round(self.odleglosc, 0))

p1 = Punkt2D(2, 5) #tworzymy obiekty
p2 = Punkt2D(4, 5)
p3 = p1 + p2
print(p3.x)
print(p3.y)

print(p1 < p2)
print(p1.odleglosc)
print(p2.odleglosc)

print(p1 == p2)
print(p2 == p2)

print(len(p3))
print(p3.odleglosc)
