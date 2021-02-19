import os

from Fonctionnalites.listen import ecouter
from Fonctionnalites.speak import speak

def addShoppingList(question):
    """
    Ajoute un élément à la liste de course
    :param question: la demande de l'utilisateur
    """
    if not os.path.exists(f'memo_output/shoppingList.txt'):
        open(f'memo_output/shoppingList.txt', 'w')

    # L'élément à ajouter dans la liste de course
    toAdd = question.split("ajoute à la liste de courses ")[1]
    print(toAdd)

    with open("memo_output/shoppingList.txt", "r") as f:
        lines = f.readlines()

    exist = False

    for line in lines:
        if line.replace("\n", "") in toAdd:
            speak(f'{toAdd} existe déjà dans votre liste de courses')
            exist = True
            break

    if exist is False:
        with open("memo_output/shoppingList.txt", "a") as f:
            f.write(toAdd + "\n")
        speak(f'{toAdd} a bien été ajouté à votre liste de course')


def deleteItemShoppingList(question):
    """
    Supprimer un élément de la liste de course
    :param question: la demande de l'utilisateur
    """
    # L'élément à supprimer de la liste de course
    toDelete = question.split("supprime de la liste de courses ")[1]
    found = False

    # On vérifie si l'item existe dans la liste de course et on le supprime s'il est trouvé
    with open("memo_output/shoppingList.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if toDelete in line:
            found = True
            with open("memo_output/shoppingList.txt", "w") as f:
                for line in lines:
                    if line.replace("\n", "") in toDelete:
                        continue
                    else:
                        f.write(line)
            speak(f'{toDelete} a bien été supprimé de la liste de course')

    if found is False:
        speak(f"{toDelete} n'existe pas dans votre liste de course")


def removeShoppingList():
    """
    Supprimer toute la liste de course
    :param question: la demande de l'utilisateur
    """
    speak("êtes-vous sur de vouloir vider la liste de course ?")
    reponse = ecouter()
    if reponse.lower() == "oui":
        with open("memo_output/shoppingList.txt", "w") as f:
            f.write("")
        speak("La liste de course a bien été vidé")
    else:
        speak("La liste de course n'a pas été vidé")