def funkcja(f, liczba):
    return f(liczba)

print(funkcja(lambda x: x * x, 3)) # 3 do kwadratu
####
def kwadrat(x):
    return x * x
print(kwadrat(5)) #5 d kwadratu
#####
wyn = (lambda x: x * x)(5) # 5 do kwadratu
print(wyn)
####
lam = lambda x: x * x
print(lam(5)) #kolejny sposób zliczenia 5 do kwadratu
####

lam2 = lambda x, y: x * y #dla lambdy podajemy więcej argumentów aniżeli 1 jak wyżej
print(lam2(2, 3))

print((lambda x, y: x + y)(5, 6)) #zrobienie funkcji lambda w jedenj linijce
