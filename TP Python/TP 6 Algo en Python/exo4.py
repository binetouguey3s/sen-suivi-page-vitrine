# nombre = int(input("Entrez un nombre : "))
# fact = 1
# if nombre >= 0:
#     for i in range(1, nombre + 1):
#         fact = fact * i
#     print("Le factoriel de", nombre, "est", fact)
# else:
#     print("Le factoriel de", nombre, "n'existe pas")

# refaire avec fonction1

# def factoriel(n: int):
#     fact = 1
#     if n >= 0:
#         for i in range(1, n + 1):
#             fact = fact * i
#         print("Le factoriel de", n, "est", fact)
#     else:
#         print("Le factoriel de", n, "n'existe pas")

# Refaire avec fonction2

def factoriel(n):
    """Calcule n! pour n entier >= 0 (itératif)."""
    if n < 0:
        raise ValueError("Le factoriel n'est pas défini pour les nombres négatifs.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def demander_et_afficher_factoriel():
    n = int(input("Entrez un entier >= 0 pour calculer son factoriel : "))
    try:
        print(f"{n}! = {factoriel(n)}")
    except ValueError as e:
        print("Erreur :", e)

# Appel
if __name__ == "__main__":
    demander_et_afficher_factoriel()
