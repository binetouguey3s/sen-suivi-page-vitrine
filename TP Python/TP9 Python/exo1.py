#Gestion de stock (Variables, Saisie et Condition) 
# Demandez à l'utilisateur de saisir le stock initial de produits.
# Demandez le nombre de produits vendus aujourd'hui.
# Calculez et affichez le stock restant.
# Si le stock restant est strictement inférieur à 10, affichez le message :
# "Attention : stock faible, penser au réapprovisionnement."

stock_initial = int(input("Veuillez saisir le stock initilal de produits: "))
produits_vendus = int(input("Donnez le nombre de produits vendus aujourd'hui:"))
stock_restant = stock_initial - produits_vendus
print("Le stock restant est de : ", stock_restant)
if stock_restant < 10:
    print("Attention : stock faible, penser au réapprovisionnement.")

    