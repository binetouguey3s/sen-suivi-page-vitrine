# nombre = int(input("Entrez un nombre: "))

# for i in range(1, 11):
#     print(nombre, "x", i, "=", nombre * i)


# refaire le programme en utilisant une fonction
n = int(input("Entrez un nombre: "))
def table_multi(n: int):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

table_multi(n)




