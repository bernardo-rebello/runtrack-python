def echanger_premiere_et_derniere(liste):
    # Vérifie si la liste non est vide
    if len(liste) > 0:
        # Échange les valeurs de la première et de la dernière case
        liste[0], liste[-1] = liste[-1], liste[0]

# Exemple d'utilisation
la_liste = [1, 2, 3, 4, 5]
print("Avant l'échange :", la_liste)

echanger_premiere_et_derniere(la_liste)
print("Après l'échange :", la_liste)