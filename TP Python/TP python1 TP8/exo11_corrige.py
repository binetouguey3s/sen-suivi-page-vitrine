# Simulation de diagnostic Covid-19

def questionnaire():
    print('Répondez par oui ou non aux questions suivantes : \n')

    questions = {
        'fievre': 'Avez-vous de la fièvre ? ',
        'toux_seche': 'Avez-vous une toux sèche ? ',
        'perte_odorat': "Avez-vous perdu l'odorat ? ",
        'respiration': 'Avez-vous des difficultés à respirer ? ',
        'courbatures': 'Avez-vous des courbatures ? '
    }

    symptomes = {}

    for symptome, question in questions.items():
        while True:
            reponse = input(question).lower()

            if reponse == 'oui':
                symptomes[symptome] = True
                break
            elif reponse == 'non':
                symptomes[symptome] = False
                break
            else:
                print('Répondez uniquement par oui ou non.\n')

    return symptomes


def covid_diagnostic(symptomes):

    point_symptome = {
        'fievre' : 2,
        'toux_seche' : 1,
        'perte_odorat': 3,
        'respiration': 4,
        'courbatures': 2
    }
    
    score = 0

    for symptome, present in symptomes.items():
        if present and symptome in point_symptome:
            score = score + point_symptome[symptome]
    

    if score >= 5:
        recommandation = 'Risque élevé : test recommandé'
    elif score >= 2:
        recommandation = 'Risque modéré : test conseillé'
    else:
        recommandation = 'Risque faible : test inutile'
    
    return score, recommandation




symptomes_patient = questionnaire()

score, avis = covid_diagnostic(symptomes_patient)

print()

print(f'Score = {score}')
print(f'Conclusion = {avis}')