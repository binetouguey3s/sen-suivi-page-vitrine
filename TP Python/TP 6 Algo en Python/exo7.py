# mot_correct = "1234a"
# tentative= 0
# while tentative < 3:
#     mot = input("Entrez le mot de passe : ")
#     if mot == mot_correct:
#         print("Accès autorisé")
#         break
#     else:
#         tentative += 1
#         print("Le mot de passe est incorrect. Vous avez tente:", tentative, "fois")
# if tentative == 3:
#     print("Compte bloqué")

#refaire la fonction
def verifier_mot_de_passe(mot_correct="1234a", max_tentatives=3):
    tentatives = 0
    while tentatives < max_tentatives:
        saisie = input("Entrez le mot de passe : ")
        tentatives += 1
        if saisie == mot_correct:
            print("Accès accordé.")
            return True
        else:
            print("Mot de passe incorrect.")
            reste = max_tentatives - tentatives
            if reste > 0:
                print(f"Il vous reste {reste} tentative(s).")
    print("Compte bloqué.")
    return False

# Appel
if __name__ == "__main__":
    verifier_mot_de_passe()
