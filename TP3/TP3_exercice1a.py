# calcul de la somme des N

N=-1
while(N<=0):
    N = int(input("saisir un nombre entier positif"))

somme=0
for i in range (1,N+1,1):
    somme+= i
    print(f"somme à n = {i} : {somme} ")

