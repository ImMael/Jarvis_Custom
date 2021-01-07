from playsound import playsound
from Fonctionnalites.listen import ecouter
from Fonctionnalites.speak import speak
from Fonctionnalites.whatDayToday import whatDayToday
from Fonctionnalites.whatTimeIsIt import whatTimeIsIt
from Fonctionnalites.whatWeather import whatWeather, getCity


def repondre():
    # speak("Bonjour, que puis-je pour vous ?")
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
    elif "météo" in question:
        whatWeather( getCity(question) )
    else:
        playsound('arouf-gangsta-begaye.wav')