print(" , ".join(["a", "b", "c"])) # rozdziela listę przecinkami
print("Witaj Świecie".replace("Witaj", "Cześć")) #replace - zamienia witaj na cześć
print("To jest zdanie".startswith("To")) # startswith sprawdza tylko czy zdanie zaczyna się od podanego ciągu znaków "to"
print("To jest zdanie".endswith("."))
print("j" in "To jest zdanie.") # czy j jest w podanym zdaniu

print("To jest zdanie.".upper()) #upper - konwertuje na duże litery
print("To Jest Zdanie.".lower()) # lower - konwertuje na małe litery

print("_____________")

lista =[10, 20, 26, 36, 40]

if all([i % 2 == 0 for i in lista]): #all - sprawdza  dla wszystkich paramentrów
    print("Wszystkie parzyste")


if any([i % 2 == 0 for i in lista]): #any - chociaż jedna z wybranych
    print("Chociaż 1 parzysta")

for i in enumerate(lista): #enumerate - numeruje argumenty na naszej liście
    print(i)
    print(i[0] +1, "-", i[1])