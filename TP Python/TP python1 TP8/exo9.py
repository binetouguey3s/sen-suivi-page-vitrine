nombres = []
for i in range(1,5):
    try:
        nombre=int(input(f"Donner le nombre:{i+1} :"))
        nombres.append(nombre)
    except ValueError:
        print("Saisir un nombre correct")
somme = sum(nombres)
moyenne= somme / len(nombres) 
maximum = max(nombres)
minimum =  min(nombres)
print(f"La somme des nombres est: {somme}")
print(f"La moyenne des nombres est: {moyenne}")
print(f"Le maximum des nombres est: {maximum}")
print(f"Le minimum des nombres est: {minimum}")

