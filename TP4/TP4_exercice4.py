# élément le plus fréquent dans une liste
liste = [2, 7, 5, 6, 7, 1, 6, 2, 1,7]

max=0
nmax=0

for j in range(len(liste)):
    n=0
    for i in range(len(liste)):
        if (liste[j]==liste[i]):
            n+=1
    if n>nmax:
        nmax = n
        max = j

print(f"L'élément le plus présent est {liste[max]} qui apparait {nmax} fois")
