#definiowanie klasy "class"

class Czlowiek: # klasy piszemy z wielkiej litery w odrużnieniu od funkcji
    imie = "Sebastian"

    def przedstawSie(self, powitanie = "Ceść"):
        return powitanie + " , mam na imię " + self.imie

obiekt = Czlowiek()
print(obiekt.imie)
print(obiekt.przedstawSie("Witam"))
obiekt2 = Czlowiek()  #tworzymy obiekt 2
obiekt2.imie = "Adrian" # przypisujemy nową wartość
print(obiekt2.przedstawSie())
##########
class Czlowiek:
    def __init__(self, imie, wiek): #"init" - inicjalizacja danych, mozna zmienić dane wyjsciowe dla obiektu
        self.imie = imie
        self.wiek = wiek
    
    def przedstawSie(self, powitanie = "Ceść"):
        return powitanie + " , mam na imię " + self.imie + " lat " + str(self.wiek) + "."

obiekt = Czlowiek("Sebastian", 24) #przytworzeniu obiektów trzeba podac dwa argumenty jak powyżej w def
print(obiekt.imie)
print(obiekt.przedstawSie("Witam"))
obiekt2 = Czlowiek("Adrian", 18)  #tworzymy obiekt 2
obiekt2.imie = "Adrian" # przypisujemy nową wartość
print(obiekt2.przedstawSie())