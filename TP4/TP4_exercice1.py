def test(ent):
    while True:
        try:
            ent = int(ent)
            return ent
        except ValueError:
            try:
                ent = float(ent)
                return ent
            except ValueError:
                ent = input("Désolé la valeur saisie n'est pas un nombre entier ni réel, réessayez : ")

def affiche(liste):
    nombre=test(input("vous cherchez la table de multiplication de quel nombre? "))

    for i in range (0,10,1):
        liste.append([nombre,i,round(i*nombre,1)])
    
    print(f"Voici la table de multiplication de {nombre} :\n")

    for i in liste:
        print(f"{i[0]} * {i[1]} = {i[2]}")

print(affiche([]))

