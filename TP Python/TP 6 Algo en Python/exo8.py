# T = []
# for i in range(5):
#     nombre = float(input("Entrez un nombre : "))
#     T.append(nombre)
# for i in range(4):
#     for j in range(i + 1, 5):
#         if  T[j] < T[i]:
#             temp = T[i]
#             T[i] = T[j]
#             T[j] = temp
# print("Les nombres en ordre croissant :")
# for nombre in T:
#     print(nombre)


# refaire avec fonction tri 

def cinq_et_tri():
    nombres = []
    for i in range(1, 6):
        x = float(input(f"Entrez le nombre {i} : "))
        nombres.append(x)
    nombres_triees = sorted(nombres)
    print("Nombres en ordre croissant :")
    for val in nombres_triees:
        print(val, end=" ")
    print()

# Appel
if __name__ == "__main__":
    cinq_et_tri()
