import os
import datetime

def afficher_info_fichier(fichier):
    taille = os.path.getsize(fichier)
    date_modification_timestamp = os.path.getmtime(fichier)
    date_modification = datetime.datetime.fromtimestamp(date_modification_timestamp)

    print(f"Nom du fichier : {fichier}")
    print(f"Taille en octets : {taille}")
    print(f"Date de dernière modification : {date_modification}")
    print()

def verification_fichiers(fichier1, fichier2):
    if os.path.isfile(fichier1):
        afficher_info_fichier(fichier1)
    else:
        print(f"Le fichier {fichier1} n'existe pas.")

    if os.path.isfile(fichier2):
        afficher_info_fichier(fichier2)
    else:
        print(f"Le fichier {fichier2} n'existe pas.")

    if os.path.isfile(fichier1) and os.path.isfile(fichier2):
        date_modification_fichier1 = os.path.getmtime(fichier1)
        date_modification_fichier2 = os.path.getmtime(fichier2)

        if date_modification_fichier1 > date_modification_fichier2:
            print(f"Le fichier le plus récent est : {fichier1}")
        elif date_modification_fichier1 < date_modification_fichier2:
            print(f"Le fichier le plus récent est : {fichier2}")
        else:
            print("Les deux fichiers ont la même date de modification.")

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

verification_fichiers(fichier1, fichier2)
