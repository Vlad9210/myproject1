def decorator(func): #tworymy funkcję z jednym argumentem func
    def wrapper():  #funkcja bedzie opakowywała inną funkcję, dodajemy cos nad i po
        print("-------")
        func()
        print("-----")
    return wrapper()

def hello():
    print("Hello World")

hello = decorator(hello) #nadpisujemy hello jako funkcję decorator
hello()

#####

@decorator  #nadpisujemy nad def ten pierwotny decorator, udekorowujemy ta poniższą funkcję
def witaj():
    print("Witaj Świecie") #funkcja do udekorowania, przyozdobienia

witaj()
