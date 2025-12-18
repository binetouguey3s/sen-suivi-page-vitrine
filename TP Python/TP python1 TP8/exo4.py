def nombre():
    try:
        a = int(input("Entrez un nombre entier : "))
    except ValueError:
        print("Veuillez entrer un entier.")
        return None
    if a % 2 == 0:
        print("Le nombre est pair")
    else:
        print("Le nombre est impair")
    return a