def saisie_notes_et_coefficients():
    notes = []
    coefficients = []

    for i in range(5):
        try:
            saisie = input(
                f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant (séparés par un espace) : ")
            note, coefficient = map(float, saisie.split())
            notes.append(note)
            coefficients.append(int(coefficient))
        except ValueError:
            print("Erreur de saisie. Veuillez entrer des valeurs valides.")

    return notes, coefficients


def calcul_moyenne_generale(notes, coefficients):
    somme_notes_coefficients = sum(note * coef for note, coef in zip(notes, coefficients))
    somme_coefficients = sum(coefficients)

    moyenne_generale = somme_notes_coefficients / somme_coefficients
    return moyenne_generale


def est_admis(moyenne_generale, notes):
    return moyenne_generale > 10 and all(note >= 8 for note in notes)


notes, coefficients = saisie_notes_et_coefficients()

moyenne_generale = calcul_moyenne_generale(notes, coefficients)

if est_admis(moyenne_generale, notes):
    print(f"L'étudiant est admis avec une moyenne générale de {moyenne_generale:.2f}.")
else:
    print(f"L'étudiant n'est pas admis avec une moyenne générale de {moyenne_generale:.2f}.")
