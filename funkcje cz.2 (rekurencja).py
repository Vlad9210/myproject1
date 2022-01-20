def func(x):
    return x * x # x * x podniesione do kwadratu

zmienna = func
print(zmienna(5))

def func2(f1, x): #f1 czyli funkcja 1
    return f1(x) * x

print(func2(func, 5)) #najpierw liczy pierwszą funkcją "func" i póxniej + druga "func2"

def silnia(x): # silnia z !3 = 3 * 2 * 1 = 6
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1) #rekurencja - funkcja wywołuje sama siebie wewnatrz swego ciała

print(silnia(5))
print(silnia(4))