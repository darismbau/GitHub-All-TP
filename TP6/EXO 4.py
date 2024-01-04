import random
## Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr' valeurs
## comprises entre 'vmin' et 'vmax'…
def generer(nbr, vmin, vmax):
    Tbl = []
    for i in range(nbr):
        Tbl.append(random.randint(vmin, vmax))
    return Tbl

## Fonction combienInferieur(table, vseuil) pour compter le nombre de valeurs
## d'un tableau 'table' inférieures à la valeur 'vseuil'…
def combienInferieur(table, seuil):
    count =0
    for k in table:
        if k < seuil :
            count += 1
    return count




nb = int(input("VEULLIEZ CHOISIR LE NOMBRE DE VALEURS A GENERER : "))
vmin = int(input("VEULLIEZ CHOISIR LA VALEUR MINIMUM : "))
vmax = int(input("VEULLIEZ CHOISIR LA VALEUR MAXIMUM : "))

choix = input("VOULEZ VOUS CHOISIR UN SEUIL (30 par défaut) OUI(O) ou NON(N) : 10")
if choix == "O":
    seuil = int(input("VEUILLEZ CHOISIR LE SEUIL : "))
else: 
    seuil = 30
        

print(f"Générer {nb} nombres entiers entre {vmin} et {vmax}")
tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)
total = combienInferieur(tab, seuil)
print(f"Il y en a {total} inférieurs à {seuil}")