a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print(f"Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print(f"Permutation: a ==> b, b ==> c, c ==> a")

temp = a
a = b
b = c
c = temp

print(f"Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)