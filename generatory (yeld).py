def gen():
    i = 0
    while i < 5:
        yield i #yield podobne do return zwraca tylko nie przerywa danej funkcji, moze wykonywac sie kilka razy
        i += 1

for i in gen(): #for - petla obiektowa
    print(i)

print(list(gen()))
##### zwraca wartości parzyste
def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1
for i in parzyste(16): #pętla od 0 do 16
    print(i)

print(list(parzyste(30))) #wyswietlamy liczby parzyste do 30 w formie listy

