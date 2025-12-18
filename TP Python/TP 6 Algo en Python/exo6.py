# nombre = []
# maximum = nombre
# minimum = nombre
# for i in range(0, 3):
#     nombre = input(f"Entrez un nombre {i+1} : ")
#     while not nombre.isdigit():
#         nombre = input(f"Entrée invalide. Entrez un nombre valide {i+1} : ")
#     if nombre > maximum:
#         maximum = nombre
#     if nombre < minimum:
#         minimum = nombre
# print("Le plus grand nombre est :", maximum)
# print("Le plus petit nombre est :", minimum)

# refaire avec fonction
def max_et_min_n_entrees(n):
    print(f"Veuillez entrer {n} nombres (entier ou décimal).")
    valeurs = []
    for i in range(1, n + 1):
        x = float(input(f"Nombre {i} : "))
        valeurs.append(x)
    maximum = max(valeurs)
    minimum = min(valeurs)
    return maximum, minimum

def demander_100():
    maxi, mini = max_et_min_n_entrees(3)
    print("Le plus grand élément est :", maxi)
    print("Le plus petit élément est :", mini)

# Appel
if __name__ == "__main__":
    demander_100()
