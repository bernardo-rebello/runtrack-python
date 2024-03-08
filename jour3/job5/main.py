def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur: Division par zéro"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur: Division par zéro"
    else:
        return "Opérateur non reconnu"

resultat_addition = calcule(5, '+', 3)
resultat_multiplication = calcule(4, '*', 2)

print(resultat_addition) 
print(resultat_multiplication) 