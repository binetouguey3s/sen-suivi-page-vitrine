mdp_correct = "python123"
tentative = 3
while tentative > 0:
    mdp_saisi = input("Saisir le mot de passe:")
    if mdp_saisi == mdp_correct:
        print("Acces autorise")
        break
    else:
        print("Acces refuse")
        tentative -= 1
        if tentative == 0:
            print("Nombre de tentatives depasse. Acces bloque.")
            break
        else:
            print(f"Il vous reste {tentative} tentative(s).")
    
    