from Fonctionnalites.answer import *
from Fonctionnalites.listen import ecouter
from Fonctionnalites.speak import speak
from Fonctionnalites.memo import check_memo


while True:
    check_memo()

    appel = ecouter()
    if appel != None:
        try:
            if "Jarvis" in appel:
                speak("oui je t'écoute")
                playsound("soundnotif.wav")
                repondre()
        except TypeError:
            pass


# NE PAS SUPPRIMER => SERT A TESTER SANS PARLER
# repondre()
# exit()
