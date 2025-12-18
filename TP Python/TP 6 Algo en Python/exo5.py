# somme = 0
# for i in range(10):
#     nombre = float(input("Entrez un nombre : "))
#     somme += nombre
# moyenne = somme / 10
# print("La somme est:", somme)
# print("La moyenne est:", moyenne)

# refaire avec fonction
def somme_et_moyenne(nombres):
    s = sum(nombres)
    moyenne = s / len(nombres) if nombres else 0
    return s, moyenne

def demander_10_et_afficher():
    nombres = []
    for i in range(1, 11):
        x = float(input(f"Entrez le nombre {i} : "))
        nombres.append(x)
    s, m = somme_et_moyenne(nombres)
    print(f"Somme = {s}")
    print(f"Moyenne = {m}")

# Appel
if __name__ == "__main__":
    demander_10_et_afficher()

