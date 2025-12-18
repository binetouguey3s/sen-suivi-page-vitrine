# Programme d'évaluation du risque de COVID-19 basé sur les symptômes
def question():
    print("Répondez aux questions suivantes par oui ou non.\n") 

    questions = {
        "fievre": "Avez-vous de la fièvre ? ",
        "toux_seche": "Avez-vous une toux sèche ? ",
        "fatigue": "Vous sentez-vous fatigué(e) ? ",
        "troubles": "Avez-vous des troubles respiratoires ? ",
        "courbatures": "Avez-vous des courbatures ? ",
        "tension": "Avez-vous une tension artérielle élevée ? "
    }

symptomes = {}

for symptome, question in questions.items():
    while True:
        reponse = input(questions).lower()

        if reponse == "oui":
            symptomes[symptome] = True
            break
        elif reponse == "non":
            symptomes[symptome] = False
            break
        else:
            print("Veuillez repondre uniquement par oui ou non.\n ")
    return symptomes

def covid_diagnostic(symptomes):

    point_symptome = {
        'fievre': 2,
        'toux_seche': 1,
        'fatigue': 1,
        'troubles': 3,
        'courbatures': 2,
        'tension': 2
    }

    score = 0
    for symptome, present in symptomes.items():
        if present and symptome in point_symptome:
            score = score + point_symptome[symptome]
    if score >= 5:
        recommandation = "Risque élevé : test recommandé"
    elif score >= 2:
        recommandation = "Risque modéré : test conseillé"
    else:
        recommandation = "Risque faible : test inutile"
    return score, recommandation


symptomes_patient = questionnaire()
score, avis = covid_diagnostic(symptomes_patient)

print()

print(f"Votre score de risque est de : {score}")
print(f"Avis médical : {avis}")

#Fin du programme
