# Fusionner deux listes (Création de listes) 🤝
# Demandez 3 nombres à l’utilisateur pour constituer une première liste (Liste A).
# Demandez 3 autres nombres à l’utilisateur pour constituer une deuxième liste (Liste B).
# Créez une troisième liste (Liste C) qui contient tous les éléments de la Liste A suivis de tous les éléments de la Liste B.
# Affichez la Liste C.

Liste_A = []
i = 0
for i in range(3):
    nombre = int(input("Saisissez un nombre pour la Liste_A :"))
    Liste_A.append(nombre)

Liste_B = []
i = 0
for i in range(3):
    nombre = int(input("Saisissez un nombre pour la Liste_B:"))
    Liste_B.append(nombre)
Liste_C = Liste_A + Liste_B
print("La Liste_C est :", Liste_C)
  