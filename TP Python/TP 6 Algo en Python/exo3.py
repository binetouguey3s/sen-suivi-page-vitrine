# print("Les nombres pairs de 1 a 50 sont: \n")
# i = 1
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i,"\n")

# Refaire le programme en utilisant une fonction

def nbre_pairs_1_50():
    print("Nombres pairs entre 1 et 50 :")
    for n in range(1, 51):
        if n % 2 == 0:
            print(n, end=" ")
    print()

if __name__ == "__main__": # Permet d'exécuter le code uniquement si le script est exécuté directement
    nbre_pairs_1_50() # Appel de la fonction

