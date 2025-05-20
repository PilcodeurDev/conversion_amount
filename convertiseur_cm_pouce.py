"""
Enoncé de l'exercice :

Créer un programme qui permet de convertir une mesures de centimètre (cm) en pouces (inch) et inversement.
1) Trouver la valeur de conversion pour cet deux deux unitées de mesure.
2) Demander à l'utilisateur dans quel sens il souhaite faire la conversion.
3) Demander la mesure à converture.
4) Faire la conversion et afficher le resultat.

    1 cm = 0.394 pouce
    1 pouce = 2.54 cm
"""

# Conversion() sert à convertir une unitée de mesure ou quitter le programme
def conversion(unit1: str, unit2: str, factor: float):
    # 3) Demander la mesure à convertir ou quitter.
    answer = input(f"Conversion {unit1} en {unit2} (ou 'q' pour quitter) : ")
    # Si l'utilisateur veux partir, il tape "q". La fonction return vrai.
    if answer == "q":
        return True
    # conversion de la virgule en point pour un chiffre a décimal.
    answer.find(",")
    user_string = answer.replace(",", ".")
    try:
        # conversion de la string en float.
        user_amount = float(user_string)
    except ValueError:
        print("ERREUR : veuillez rentrer une valeur numérique ")
        return conversion(unit1, unit2, factor)
    # Conversion des unitées
    new_amount = round(user_amount * factor, 2)
    print(f"{user_amount} {unit1} représente {new_amount} {unit2}.")
    return False

print("")
print(" 1. Conversion de centimètre en pouce")
print(" ou")
print(" 2. Conversion de pouce en centimètre")
print("")
user_choice = input("Choisissez le sens de conversion (1 ou 2) : ")

# Tant que c'est vrai :
while True :
    if user_choice == "1":
        # Si c'est vrai, la boucle s'arrête.
        if conversion("cm", "pouce", 0.394):
            break

    elif user_choice == "2":
        if conversion("pouce", "cm", 2.54):
            break
