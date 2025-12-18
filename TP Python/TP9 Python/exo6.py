# Compter les voyelles dans une liste de mots (Boucles Imbriquées) 
# Demandez à l'utilisateur de saisir 5 mots.
# Pour chacun des 5 mots saisis :
# Comptez le nombre de voyelles qu'il contient (A, E, I, O, U, Y, en majuscules et minuscules).
# Affichez le mot suivi du nombre de voyelles trouvées.

# methode1

# voyelles = "AEIOUYaeiouy"
# Liste_mots = []
# for i in range(7):
#     mot = input("Saisissez un mot : ")
#     Liste_mots.append(mot)
#     compter_voyelles = 0
#     for lettre in Liste_mots[i]:
#         if lettre in voyelles:
#             compter_voyelles += 1
#             print(f"Le mot '{mot}' contient {compter_voyelles} voyelles).")



# methode2

voyelles = "AEIOUYaeiouy"
Liste_mots = []
for i in range(7):
    mot = input("Saisissez un mot : ")
    Liste_mots.append(mot)
    if len(Liste_mots) > 0:
        for mot in Liste_mots:
            compter_voyelles = 0
        for lettre in mot:
            if lettre in voyelles:
                compter_voyelles += 1
        print(f"Le mot '{mot}' contient {compter_voyelles} voyelles).")
    else:
        print("Aucun mot saisi.")
