tour = int(input("COMBIEN DE NOTES : "))
Sommes = 0
sommeCoef = 0

for i in range (tour):
    Notes = str(input("Veuillez entrer la note du module 1 et le coefficient correspondant : "))

    S2 = Notes.split()
    S3 = float(S2[0])
    S4 = float(S2[1])
    Multi = S3 * S4
    Sommes += Multi
    sommeCoef += S4


moyenne = Sommes / sommeCoef

print (f"LA MOYENNE EST {round(moyenne, 1)}")
