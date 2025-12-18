# Répartition de nombres (Tri selon la parité) 🌓
# Demandez à l'utilisateur de saisir 8 nombres.
# Placez tous les nombres pairs dans une liste A.
# Placez tous les nombres impairs dans une liste B.
# Affichez la liste A et la liste B séparément.

Liste_A = []
Liste_B = []
i = 0
for i in range(8):
    nombre = int(input("Saisissez les nombres:"))
    if  nombre % 2 == 0:
        Liste_A.append(nombre)
        print("Le nombre est:",nombre)
    else:
        Liste_B.append(nombre)
        print("Le nombre est :", nombre)
        print("La Liste des nombres pairs est :", Liste_A)
        print("La Liste des nombres impairs est :", Liste_B)
