plik = open("analiza tekstu.txt", "r")
tekst = plik.read()
plik.close()

#ile dana litera wystepuje w tekscie

def policz(txt, znak):
    licznik = 0
    for z in txt:
        if z == znak:
            licznik += 1
    return licznik

print(policz(tekst, "a") + policz(tekst, "A"))
print(policz(tekst.lower(), "a"))
print(policz(tekst.lower(), "z"))

#policzymy ile każda litera zajmuje procentowo całego tekstu

for z in "abcdefghijklmnoprstuwxyz":
    ile = policz(tekst.lower(), z)
    procent = 100 * ile / len(tekst) #len - zlicza długość, z nie litera a argument
    print("{0} - {1} - {2}%".format(z.upper(), ile, round(procent, 2))) #pierwszy argument(0) która to litera , 1 - ile jest ich w tekscie, 2 - procentowo ile to jest
    