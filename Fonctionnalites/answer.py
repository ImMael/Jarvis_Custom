from playsound import playsound
from Fonctionnalites.listen import ecouter
from Fonctionnalites.speak import speak, repeat
from Fonctionnalites.time import whatDayToday, whatTimeIsIt
from Fonctionnalites.whatWeather import whatWeather, getCity
from Fonctionnalites.calcul import calculate
from textVariations import getVariations


def repondre():
    question = ecouter()
    variations = getVariations()

    # question = "Donne moi la météo à Paris s'il te plait"
    # question = "quelle heure est-il s'il te plait"

    # if "Bonjour" in question:
    #     speak('Bonjour, comment allez vous ?')
    # elif "quelle heure" in question:
    #     whatTimeIsIt()
    # elif "quel jour" in question:
    #     whatDayToday()
    # elif "répète après moi" in question:
    #     repeat(question)
    # elif "météo" in question:
    #     whatWeather( getCity(question) )
    # elif ("x" in question) or ("/" in question) or ("-" in question) or ("+" in question):
    #     calculate(question)
    # else:
    #     playsound('arouf-gangsta-begaye.wav')

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