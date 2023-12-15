#Première personne
nom1=input("Entrez le nom de la première personne :")
prenom1=input("Entrez le prénom de la première personne :")


#Deuxième personne
nom2=input("Entrez le nom de la deuxième personne :")
prenom2=input("Entrez le prénom de la deuxième personne :")


#Minsucule et majuscules
nom1=nom1.upper()
prenom1=prenom1.capitalize()
nom2=nom2.upper()
prenom2=prenom2.capitalize()

#affiche dans l'ordre alphabétique

if nom1<nom2:
    print(prenom1,nom1)
    print(prenom2,nom2)
elif nom1>nom2:
    print(prenom2,nom2)
    print(prenom1,nom1)
else:
    if prenom1 < prenom2:
        print(prenom1,nom1)
        print(prenom2,nom2)
    else:
        print(prenom2,nom2)
        print(prenom1,nom1)

