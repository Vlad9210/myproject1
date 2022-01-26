#list comprehension - wyrażenia listowe

lista = list(range(10))

nowa = [i * 2 for i in lista]
nowa2 = [i + 2 for i in lista if i % 2 == 0]
print(lista)
print("Nowa: ", nowa)
print("Nowa 2: ", nowa2)

# formatowanie String - string formatter

argumenty = ["Sebastian", 24]
tekst = "Cześć mam na imię {0} i mam {1} lat.".format(argumenty[0], argumenty[1])
print(tekst)

tekst = "Cześć mam na imię {imie} i mam {wiek} lat.".format(imie = argumenty[0], wiek = argumenty[1])
print(tekst)