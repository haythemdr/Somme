def NombresPairs(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre
    return somme


print("Entrer une liste des nombres : ")
input_user = input()

liste= [int(number) for number in input_user.split()]
resultat =NombresPairs(liste)
print("La somme des nombres pairs est :", resultat)

