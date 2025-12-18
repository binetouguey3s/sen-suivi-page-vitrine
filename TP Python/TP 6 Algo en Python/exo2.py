# A = int(input("Donnez A : "))
# B = int(input("Donnez B : "))

# temp = A
# A = B
# B = temp

# print("Finalement après échange: A =", A, ", B =", B)

# refaire le programme en utilisant une fonction
def echanger(a, b):
    temp = a
    a = b
    b = temp
    return a, b   

a = int(input("Donnez a : "))
b = int(input("Donnez b : "))
a, b = echanger(a, b)
print("Finalement après échange: a =", a, ", b =", b)