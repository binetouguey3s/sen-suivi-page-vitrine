def risques(symptomes):
    score_risque = 0
    symptomes_list = [True, False, True, False]  
    for i in range(0, len(symptomes_list)):
        score_risque += int(symptomes_list[i])
    print(f"Les symptomes :score_risque= {score_risque}")
    return score_risque

symptomes_patient = {
    "fievre": True,
    "toux_seche": False,
    "fatigue": True,
    "troubles": False
}
score_risque = risques(list(symptomes_patient.values()))
print(f"Score de risque est de: {score_risque}")
if score_risque >= 2:
    print("Le patient doit faire un test COVID-19")
else:
    print("Le patient n'a pas besoin de faire un test COVID-19")


        

