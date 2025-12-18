nombres = []
for i in range(1,6):    
    try:
        nombres = int(input(f"Donner le {i}er nombre "))
    except ValueError:
        print("Donner un nombre dans la liste.")
        for nombres in nombres :
            print(f"Les nombres sont: {nombres}")
            print(f"Le type de la variable est: {type(nombres)}")
            nombres.append(nombres)
            print(f"La liste des nombres est : {nombres}")
            nombres.sort()
print






