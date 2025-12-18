try:
    N = int(input("Entrez un entier N : "))
except ValueError:
    print("Veuillez entrer un entier valide.")
    exit(1)

if N <= 0:
    print("N doit être un entier positif.")
else:
    total = 0
    for i in range(1, N + 1):
        total += i
        print(f"Après ajout de {i} : somme = {total}")
    print(f"\nLa somme de 1 à {N} est {total}")