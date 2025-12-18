# Recherche de doublons dans une liste (Boucle et Vérification) 
# Demandez à l'utilisateur de saisir 7 nombres pour former une liste.
# Vérifiez si cette liste contient au moins deux fois la même valeur c’est-a-dire un doublon.
# Affichez :
# "Doublons trouvés" si au moins une valeur est répétée.
# "Aucun doublon" sinon.

# Liste = []
# for i in range(1,8):
#     nombre = int(input("Saisissez les nombres:"))
#     Liste.append(nombre)
#     print("La liste est:",Liste)
# if Liste.count(nombre) > 1:
#     print("Doublons trouvés")
# else:
#     print("Aucun doublon")

# methode classique 1

# Liste = []
# compteur_doublon = 0
# for i in range(1,8):
#         nombre = int(input("Saisissez les nombres:"))
#         Liste.append(nombre)
#         print("La Liste est :", Liste)
# for i in range(len(Liste)):
#         for j in range(i+1, len(Liste)):
#             if Liste[i] == Liste[j]:
#                 compteur_doublon += 1
#             break
# if compteur_doublon > 0:
#     print("Doublons trouvés avec le nombre:",nombre,"est repeté",compteur_doublon + 1,"fois")
# else:
#     print("Aucun doublon")
# fin

# methode classique 2

def recherche_doublons():
    nombres = []

    for i in range(7):
        valeur = int(input("Entrez un nombre : "))
    nombres.append(valeur)

    doublon_trouve = False

    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            if nombres[i] == nombres[j]:
                doublon_trouve = True

    if doublon_trouve:
        print("Doublons trouvés")
    else:
        print("Aucun doublon")
