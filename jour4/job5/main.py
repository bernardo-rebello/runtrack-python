def remplacer_par_somme_voisins(lst, index):
    # Vérifie si l'index est valide
    if 0 <= index < len(lst):
        # Calcule somme voisins L[2] et L[4]
        somme_voisins = lst[2] + lst[4]
        # Remplace L[3] par somme des voisins
        lst[index] = somme_voisins

# Crée liste d'au moins 5 entiers
L = [1, 2, 3, 4, 5]

# Affiche deuxième valeur de la liste
print("Deuxième valeur de la liste :", L[1])

# Appele la fonction pour remplacer L[3] par la somme des voisins L(2) et L(4)
remplacer_par_somme_voisins(L, 3)

# Affiche le tableau après la modification
print("Tableau après modification :", L)

# Affiche dernière valeur de la liste
print("Dernière valeur de la liste :", L[-1])