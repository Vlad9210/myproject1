plik = open("test.txt", "a") #open - otwieranie plików
print(plik.writable())
if plik.writable():  #jesli plicz jest do zapisu
    plik.write(input("Wprowadź tekst: ") + "\n")
plik.close()


plik = open("test.txt", "r")

if plik.readable():
    tekst = plik.read()
    print(tekst)


plik = open("test.txt", "r")

if plik.readable():
    print("Zawartość pliku: ")
    tekst = plik.readlines()
    print(tekst)
    for l in tekst:
        print(l)