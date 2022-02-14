class Test:
    def __new__(cls): #uzyliśmy metody "New"
        print("Hello Class")
obj = Test() #obj - object, obiekt

class Test:
    def __del__(self): # metoda magiczna "del" - destruktor (przeciwnie do konstruktor), kiedy kończy się życie zaczyna działać destruktor
        print("Bye Class")

obj = Test()
obj2 = obj
lista = [obj2]
del obj

print("Koniec") # "Bye Class" wykona się na końcu juz po "Koniec"



