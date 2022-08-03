"""
écrire la table de multiplication
afficher_table_multiplication(n)
definir le min = 0 ou 1 / max = 10 ou 12
erreur : si min > max => erreur
"""
#NB_MIN = 1
#NB_MAX = 10

def afficher_table_multiplication(n):
    #multiplcateur_str = input("Table de multiplication par : ")
    min_str = input("Entrer la valeur minimale: ")
    max_str = input("Entrer la valeur maximale: ")
    min = int(min_str)
    max = int(max_str)
    #n = int(multiplcateur_str)
    #print(f"Table de multiplication par {n}")
    print(f"la valeur minimale est : {min}")
    print(f"la valeur maximale est : {max}")

    """try:
        if min != int and max != int:
            return print("Entrer des entiers")

        if min > max:
            return print("Votre min est supérieur à votre max")

        return print("Entrer les bonnes valeurs")"""

    try:
        if min > max:
            return print("Erreur: Votre min est supérieur à votre max")
    except:
        return print("Entrer des valeurs entières")
        #raise error

    for i in range(min, max+1):
        multiplie = i*n
        print(i, "*", n, "=", multiplie)

afficher_table_multiplication(3)