# factorielle

#méthode 1 while

def factw(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact
#méthode 2 for
def factf(n):
    fact = 1
    if n > 1:
        for i in range(1, n + 1, 1):
            fact *= i
    return fact

""" Fonction et recursivité """

def fact(p):
    f = -1
    if p == 0 or p == 1:
        f = 1
    else:
        f = p * fact(p - 1)
    return f

# MTx

fa=-1
while (fa<0):
    fa=int(input("saisir un entier positif "))

choix = (int)(input("choisir la méthode (1 for, 2 while 3 recursivité) "))

if (choix == 1):
    res = factf(fa)
elif choix == 2:
    res = factw(fa)
else:
    res = fact(fa)


print(f"{fa}! = {res}")