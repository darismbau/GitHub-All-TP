entier = int(input("entrez un nombre entier:"))

if (entier <0):
    aff = "un nombre négatif"
    if (entier%2==0):
        aff += " pair"
    else:
        aff += " impair"
elif entier > 0:
    aff = "un nombre positif"
    if (entier%2==0):
        aff += " pair"
    else:
        aff += " impair"
else:
    aff = "zéro (et il est pair)"

print(f"{entier} est {aff}")