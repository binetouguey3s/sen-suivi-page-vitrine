# Inverser une chaîne de caractères 
# Demandez à l'utilisateur de saisir une phrase ou un mot.
# Créez et affichez une nouvelle chaîne de caractères qui est l'inverse de celle saisie.
# Exemple : Si l'utilisateur saisit "Cheikh", le programme doit afficher "hkiehC".

# Methode 1

def phrases():
    phrase = input("Saisaissez une phrase ou un mot : ")
    print("La phrase saisie est :", phrase)
    phrase_inversee = " "
    for mot in phrase:
        phrase_inversee = phrase[len(phrase)-1 - phrase.index(mot)]
        print("La phrase inversée est :", phrase_inversee, "\t")

phrases() 


# Methode 2


# def inverser_mot():
#     phrase = input("Saisissez une phrase ou un mot : ")
#     phrase_inversee = phrase[:3:-1]
#     print("La phrase inversée est :", phrase_inversee)
# inverser_mot()



# Methode 3

# phrase = " "
# def inverser_phrase():
#     phrase = input("Saisissez une phrase ou un mot : ")

# phrase_inversee = ""

# i = len(phrase)-1

# while i >= 0:
#         phrase_inversee = phrase_inversee + phrase[i]
#         i = i - 1 

#         print("La phrase inversée est :", phrase_inversee)



