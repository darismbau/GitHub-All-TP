début = int(input("Donnez l’heure de début de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) :"))

while début > fin:
    print("LOCATION IMPOSSIBLE veuillez entrer en heure de début inférieur à l'heure de fin.")
    début = int(input("Donnez l’heure de début de la location (un entier) : "))
    fin = int(input("Donnez l’heure de fin de la location (un entier) :"))

while début > 24 or début < 0:
    print ("Les heures doivent être comprises entre 0 et 24 !")
    début = int(input("Donnez l’heure de début de la location (un entier) : "))

while fin > 24 or fin < 0:
    print ("Les heures doivent être comprises entre 0 et 24 !")
    fin= int(input("Donnez l’heure de fin de la location (un entier) : "))

while début == fin:
    print("Attention ! l’heure de fin est identique à l’heure de début.")
    début = int(input("Donnez l’heure de début de la location (un entier) : "))
    fin = int(input("Donnez l’heure de fin de la location (un entier) :"))


un = 0
deux = 0

if début <= 7 and fin <= 7:
    un = un + (fin - début)

elif début < 7 and fin > 7 and fin <= 17:
    un = un + ( 7 - début)
    deux = deux + (fin -7)

elif début > 7 and début <= 17 and fin > 17 :
    deux = deux + ( 17 - début)
    un = un + (fin - 17)

elif début > 17 and fin > 17:
    un = un + (fin - début)

else:
    deux = deux + (fin - début)


print ("Vous avez loué votre vélo pendant")
if un > 0:
    print(un , " heure(s) au tarif horaire de 1.0 euro(s)")
if deux > 0:
    print(deux , " heure(s) au tarif horaire de 2.0 euro(s)")

total = un + deux*2
print("Le montant total à payer est de ", total ," euro (s).")
