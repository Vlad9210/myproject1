print(5 == 5) # operator "==" porównuje dwie liczby
print(5 != 5) # operator "!=" różni się
print(5 <= 5) # operator "<=" mniejsze lub równa się

#instrukcje warunkowe (if)
if 5 == 5:
    print("Prawda")
print("Koniec")

#jesli falsz
if 5 > 10:
    print("Mniejsze")
if 5 <= 10:
    print("Prawda")

#warunek "else" - w każdym przeciwnym wypadku
if 5 > 10:
    print("Większe")
else:
    print("Mniejsze")

# warunek "elif" - jesli 1 warynek nie spełniony to sprawdza drugi
x = 15
y = 20
if x > y:
    print("X Większe Y")
elif x < y:
    print("X Mniejsze Y")
else:
    print("X równe Y")

#jesli x = y
x = 15
y = 15
if x > y:
    print("X Większe Y")
elif x < y: #elif można umieszczaś dowolnie ile chcesz
    print("X Mniejsze Y")
else:
    print("X równe Y")
