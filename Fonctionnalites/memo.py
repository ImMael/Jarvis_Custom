import ast
import datetime
from Fonctionnalites.speak import speak
import os

save_memo = "memo"

# fonction pour sauvegarder un memo dans u fichier txt
def memo(question):
    if not os.path.exists(f'memo_output/{save_memo}.txt'):
        open(f'memo_output/{save_memo}.txt', 'w')

    date = question.split("rappelle-moi le ")

    tache = date[1].split(" de ")

    f = open(f'memo_output/{save_memo}.txt', "a")
    text = {"date": tache[0].replace("1er", "1"),
            "memo": tache[1]}
    f.write(str(text) + "\n")
    f.close()

# Fonction pour annoncer un mémo si c'est l'heure et puis le supprimer
def check_memo():
    fr_month = (
        "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre",
        "décembre")
    date = datetime.datetime.now()
    mois = fr_month[date.month - 1]

    actualDate = f'{date.day} {mois} à {date.hour}h'

    file = open('memo_output/memo.txt', "r")
    lines = file.readlines()
    file.close()

    new_file = open("memo_output/memo.txt", "w")
    for line in lines:
        dictionary = ast.literal_eval(line)
        if actualDate in dictionary['date']:
            speak(f'Vous avez un rappel pour {dictionary["date"]}, pour {dictionary["memo"]} ')
            print(f'Vous avez un rappel pour {dictionary["date"]}, pour {dictionary["memo"]} ')
        else:
            new_file.write(line)

    new_file.close()


