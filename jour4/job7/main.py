def multiples_de_3(liste):
    # Utilise une compréhension de liste pour filtrer les multiples de 3
    multiples_de_3 = [nombre for nombre in liste if nombre % 3 == 0]
    
    # Retourne le nombre de multiples de 3
    return len(multiples_de_3)

# Exemple d'utilisation avec la liste L
L = [8, 24, 48, 2, 16]
nombres_multiples_de_3 = multiples_de_3(L)

print("Nombre de multiples de 3 dans la liste :", nombres_multiples_de_3)