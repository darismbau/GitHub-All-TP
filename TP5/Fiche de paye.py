def calculer_salaire(heures_travaillees, salaire_horaire):
    heures_normales = min(heures_travaillees, 160)
    heures_majoration1 = max(0, min(heures_travaillees, 200) - 160)
    heures_majoration2 = max(0, heures_travaillees - 200)

    salaire = heures_normales * salaire_horaire \
              + heures_majoration1 * 1.25 * salaire_horaire \
              + heures_majoration2 * 1.5 * salaire_horaire

    return salaire

heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire_total = calculer_salaire(heures_travaillees, salaire_horaire)
print(f"Le salaire total est de : {salaire_total} euros.")
