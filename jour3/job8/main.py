def lescours(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi.")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis.")
    elif type == "légume" and saison == "hiver":
        print("Carotte, topinambour, endive.")
    elif type == "légume" and saison == "été":
        print("Artichaut, aubergine, navet.")
    else:
        print("Aucune sélection correspondante.")
lescours("fruits", "hiver")
lescours("fruits", "été")
lescours("légume", "hiver")
lescours("légume", "été")
lescours("viande", "automne")  