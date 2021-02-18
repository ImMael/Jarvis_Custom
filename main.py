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
                playsound("soundnotif.wav")
                repondre()
        except TypeError:
            pass


# NE PAS SUPPRIMER => SERT A TESTER SANS PARLER
<<<<<<< HEAD
#repondre()
#exit()
=======
repondre()
exit()

# API GOOGLE SEARCH
#  AIzaSyBoi24dsIdsQ_j-qDVDSd2RVF2-EPRPwYk
>>>>>>> a40ac2639d4120eb0fab5a37e68f3382af507dfc
