# Filtrer les éléments négatifs d'une liste (Boucle et Condition)
# Demandez à l'utilisateur de saisir 10 nombres (positifs ou négatifs).
# Créez une nouvelle liste qui contient uniquement les nombres supérieurs ou égaux à 0 (nombres non négatifs).
# Affichez la nouvelle liste.

Liste1 = []
i = 0
for i in range(0,2):
    nombre = int(input("Saisissez un nombre pour la Liste1 :"))
    if nombre > 0 or nombre < 0:
        Liste1.append(nombre)
    else:
        print("Le nombre est nul")

Liste2 = []
i = 0
for i in range(0,2):
    nombre = int(input("Saisissez un nombre pour la Liste2 :"))
    if nombre >= 0:
        Liste2.append(nombre)       

    print("La liste des nombres non negatifs est :", Liste2)

