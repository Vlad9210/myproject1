def Zyczenia():
    name = input("Podaj imie");
    wishes = input("Napisz życzenia");
    print("Witaj " + name + " Życzę " + wishes)

def TakeInputFromUser(): 
    return (float(input("Podaj liczbę")));
    
def suma(number1, number2):
    return (number1 + number2);
    
    
#Zyczenia()
#print(suma(TakeInputFromUser(), TakeInputFromUser()))

def buduj_zdanie(info):
    a = info + " Jest zaletą funkcji"
    return (a)

info = "ght";
i = buduj_zdanie(info);
print(i);
