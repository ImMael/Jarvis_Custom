from Fonctionnalites.answer import *
from Fonctionnalites.listen import ecouter
from Fonctionnalites.speak import speak


while True:
    appel = ecouter()
    if appel != None:
        try:
            if "Jarvis" in appel:
                playsound("soundnotif.wav")
                repondre()
        except TypeError:
            pass
