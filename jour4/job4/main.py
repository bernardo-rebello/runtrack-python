def liste_fruits():
    fruits = ['pomme', 'cerise', 'orange', 'melon']
    fruits.insert(2, 'mangue')
    return fruits
liste_fruits_avec_mangue_en_2eme = liste_fruits()
print(liste_fruits_avec_mangue_en_2eme)
