from playsound import playsound
from Fonctionnalites.listen import ecouter
from Fonctionnalites.speak import speak
from Fonctionnalites.time import whatDayToday, whatTimeIsIt
from Fonctionnalites.whatWeather import whatWeather, getCity
from Fonctionnalites.calcul import calculate
from Fonctionnalites.translate import translate
from Fonctionnalites.disease import covcases


def repondre():
    question = ecouter()
    if "Bonjour" in question:
        speak('Bonjour, comment allez vous ?')
    elif "quelle heure" in question:
        whatTimeIsIt()
    elif "quel jour" in question:
        whatDayToday()
    elif "répète après moi" in question:
        repeatable = question.split("répète après moi")
        speak(repeatable)
    elif "traduis" in question:
        translate(question)
    elif "météo" in question:
        whatWeather( getCity(question) )
    elif ("x" in question) or ("/" in question) or ("-" in question) or ("+" in question):
        calculate(question)
    elif ("cas" in question) and (("covid" in question) or ("covit" in question)):
        country = question.split("en ")
        covcases(country[2], "cas")
    elif ("mort" in question) and (("covit" in question) or ("covid" in question)):
        country = question.split("en ")
        covcases(country[2], "morts")
    else:
        playsound('arouf-gangsta-begaye.wav')

    # waitingReponse = True
    # for variation in variations:
    #     if variation in question:
    #         try:
    #             variations[variation]()
    #             waitingReponse = False
    #             break
    #             pass
    #         except Exception as e:
    #             pass
    #         try:
    #             variations[variation](question)
    #             waitingReponse = False
    #             break
    #         except Exception as e:
    #             print(e)
    #             pass
    # if waitingReponse:
    #     playsound('arouf-gangsta-begaye.wav')