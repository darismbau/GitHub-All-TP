def decomposer_somme(somme):
    billet100 = somme // 100
    somme %= 100

    billet50 = somme // 50
    somme %= 50

    billet10 = somme // 10
    somme %= 10

    piece2 = somme // 2
    somme %= 2

    piece1 = somme

    print(f"{somme} euros, c'est donc {billet100} billets de 100, {billet50} de 50, {billet10} de 10, {piece2} pièces de 2 et {piece1} pièce 1.")

somme = int(input("Entrez une somme d'argent en euros : "))

decomposer_somme(somme)
