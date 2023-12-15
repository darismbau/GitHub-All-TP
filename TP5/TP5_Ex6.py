def taille_chaine(chaine):
    taille = 0
    while chaine[taille] != '\0' and taille < 100:
        taille += 1
    return taille

def pourcentage_voyelles(chaine, taille):
    voyelles = "aeiouyAEIOUY"
    nb_voyelles = sum(1 for char in chaine[:taille] if char in voyelles)
    pourcentage = (nb_voyelles / taille) * 100
    return pourcentage

def recherche_sous_chaine(chaine, sous_chaine):
    index = 0
    while index < len(chaine) and chaine[index:index+len(sous_chaine)] != sous_chaine:
        index += 1
    if index == len(chaine):
        return -1
    else:
        return index

def occurrences_sous_chaine(chaine, sous_chaine):
    index = recherche_sous_chaine(chaine, sous_chaine)
    occurrences = 0
    while index != -1:
        occurrences += 1
        index = recherche_sous_chaine(chaine[index+len(sous_chaine):], sous_chaine)
        if index != -1:
            index += len(sous_chaine)
    return occurrences

chaine = input("Entrez une chaîne de caractères : ")

taille = taille_chaine(chaine)
print(f"1. La taille de la chaîne est : {taille}")

pourcentage = pourcentage_voyelles(chaine, taille)
print(f"2. Le pourcentage de voyelles dans la chaîne est : {pourcentage:.2f}%")

index_sous_chaine = recherche_sous_chaine(chaine, "wagon")
if index_sous_chaine != -1:
    print(f"3. La sous-chaîne 'wagon' commence à l'index : {index_sous_chaine}")
else:
    print("3. La sous-chaîne 'wagon' n'est pas présente dans la chaîne.")

occurrences = occurrences_sous_chaine(chaine, "wagon")
print(f"4. Le nombre d'occurrences de la sous-chaîne 'wagon' est : {occurrences}")
