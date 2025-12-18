
try:
    nombre = int(input("Entrer un nombre entier : "))
except ValueError:
    print("Veuillez entrer un entier valide.")
    exit(1)
print(f"Table de multiplication de {nombre} :")
for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} * {i} = {resultat}")
