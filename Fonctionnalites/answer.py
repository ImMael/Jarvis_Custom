from playsound import playsound

from Fonctionnalites.disease import covcases
from Fonctionnalites.listen import ecouter
from Fonctionnalites.speak import speak
from Fonctionnalites.time import whatDayToday, whatTimeIsIt
from Fonctionnalites.whatWeather import whatWeather, getCity
from Fonctionnalites.calcul import calculate
from Fonctionnalites.translate import translate
# from Fonctionnalites.disease import covcases
from textVariations import getVariations


def repondre():
    """
    Permet de répondre à une demande de l'utilisateur parmis pluiseurs variations de demandes possible
    """
    question = ecouter()

    # question = "Bonjour"
    # question = "quelle heure est il"
    # question = "quel jour sommes nous"
    # question = "répète après moi bonjour tout le monde"
    # question = "quel est la météo à Paris stp"
    # question = "résultat du calcul 2.5 / 2"
    # question = "quels sont les résultat du covid en france stp"
    # question = "traduis comment allez vous en anglais"
    # question = "rappelle moi le 15 février 2021 à 15 heures"
    # question = "ajoute à la liste de course des yaourts au chocolat"
    # question = "supprime de la liste de course des yaourts au chocolat"
    # question = "peut-tu vider la liste de course stp"
    # question = "quel est le temps du trajet de Poissy à Paris"

    # question = "donne moi l'heure s'il te plait"
    # question = "donne moi la date d'aujourd'hui"
    # question = "quel temps fait-il aujourd'hui à Paris"
    # question = "donne moi le résultat de 2.5/2"
    # question = "créé moi un rappel "

    variations = getVariations()

    waitingReponse = True
    for variation in variations:
        if variation in question:
            try:
                variations[variation]()
                waitingReponse = False
                break
                pass
            except Exception as e:
                pass
            try:
                variations[variation](question)
                waitingReponse = False
                break
            except Exception as e:
                print(e)
                pass
    if waitingReponse:
        playsound('arouf-gangsta-begaye.wav')
        print("CA NE MARCHE PAS")


    # ===============================================================================================


    # if "Bonjour" in question:
    #     speak('Bonjour, comment allez vous ?')
    # elif "quelle heure" in question:
    #     whatTimeIsIt()
    # elif "quel jour" in question:
    #     whatDayToday()
    # elif "répète après moi" in question:
    #     repeatable = question.split("répète après moi")
    #     speak(repeatable)
    # elif "traduis" in question:
    #     translate(question)
    # elif "météo" in question:
    #     whatWeather( getCity(question) )
    # elif ("x" in question) or ("/" in question) or ("-" in question) or ("+" in question):
    #     calculate(question)
    # elif ("cas" in question) and (("covid" in question) or ("covit" in question)):
    #     country = question.split("en ")
    #     covcases(country[2], "cas")
    # elif ("mort" in question) and (("covit" in question) or ("covid" in question)):
    #     country = question.split("en ")
    #     covcases(country[2], "morts")
    # else:
    #     playsound('arouf-gangsta-begaye.wav')