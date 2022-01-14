wiek = 19
kasa = 40

if wiek >= 18:
    if kasa >= 35:
        print("Możesz wejść")

#film dla dorosłych
wiek = 19
kasa = 40

if wiek >= 18 and kasa >= 35:
    print("Możesz wejsc")


#film dla dzieci darmowy
wiek = 11
kasa = 15

if wiek <= 12 or kasa >= 30: #albo masz poniżej 12 lat albo masz kasę aby zapłacić
    print("Możesz wejsc")


#operator negacji "not"
wiek = 11
kasa = 40

if not wiek > 12 or kasa >= 30:
    print("Może wejsc")
else:
    print("Nie może wejsc")


# and jest ważniejsze od or
if True or False and False: 
    print("Prawda")
else:
    print("Fałsz")


if (True or False) and not False:
    print("Prawda")
else:
    print("Fałsz")