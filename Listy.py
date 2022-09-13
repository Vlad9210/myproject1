my_list = []
print (my_list)

fruits = ["Jabłko" , "Banan" , "Śliwka"]
print (fruits)


fruits = ["Jabłko"]
fruits.append ("Banan") # append - dodawanie do listy
print (fruits)
fruits.append ("Kiwi")
print (fruits)


fruits = ["jabłko" , "banan" , "sliwka"]
ret = fruits.pop() # .pop - zabiera z listy
print (ret)
print (fruits)

fruits = ["jabłko" , "banan" , "sliwka"]
print (fruits[1]) # w nawiasiach [] podajemy do jakiego elementu chcemy sie odnieść
print (fruits[0])
print (fruits[-1]) # -1 czyli odwolujemy sie do ostatniego elementu, -2 do przedostatniego
fruits[1] = "kiwi" # zmiana 2 elementu
print (fruits)

names = ["Ada" , "Bartek" , "Ola" , "Wojtek"]
names[1:3] = ["Jola"] # elementy 2 i 3  zamienia na Jola
print (names)

names = ["Ada" , "Bartek" , "Ola" , "Wojtek"]
print (len(names)) # len zlicza wielkość listy
print ("Ola" in names) # in - sprawdza czy Ola jest na liscie, jesli jest to True
print ("Aga" in names)



