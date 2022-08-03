# Les fonctions: 10 -Module d'expertise
# Elles permettent d'écrire du code maintenable
# pour bien les écrire, on aura besoin de:
# -> les définir avec la commande "def"
# -> ajouter des paramètres si necessaire
# -> faire un return
# Une fonction ne doit retourner qu'une seule valeur
# il est conseillé de faire une hiérarchie de fonction pour un travail efficace
# cad classer les fonctions des plus indépendantes au dépendantes

""" Pour la hierarchie
recuperer_et_afficher_infos_personne doit etre découpé en
    -> recuperer_infos_personne()
    -> afficher_infos_personne(nom, age)
        -> est_majeur
car une fonction ne doit faire qu'une seule chose
"""

def est_majeur(age: int): # "-> bool"   spécifie le retour de la fonction
    if age <= 0:
        return False
    if age >= 18:
        return True
    return False

def recuperer_infos_personne(numero_personne):
    nom = input(f"Nom de la personne {numero_personne}: ")
    age = input(f"Age de la personne {numero_personne}: ")
    return nom, int(age)  #permet de sauvegarder la valeur pour un usage futur

def afficher_infos_personne(numero_personne, nom, age: int):
    print(f"La personne {numero_personne} est", nom, "son age est", age, "ans")
    print("Le nom comporte", len(nom), "lettres") # print() prend plusieur paramètres


def recuperer_et_afficher_infos_personne(numero_personne):

    # On va récuperer les valeurs et les sauvegarder dans des variables
    # attention, bien respecter l'ordre comme dans la fonction principale
    nom, age = recuperer_infos_personne(numero_personne)
    afficher_infos_personne(numero_personne, nom, age)

nb_personnes = 2

for i in range(nb_personnes):
    recuperer_et_afficher_infos_personne(i+1)
    print()
print()
afficher_infos_personne("007", "James", 40)