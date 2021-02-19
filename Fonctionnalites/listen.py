import speech_recognition as sr


def ecouter():
    """
    Fonction permettant de rester sur écoute constamment
    :return la demande de l'utilisateur s'il en a fais une
    """
    ecoute = True
    r = sr.Recognizer()
    print('En écoute')
    while ecoute:
        with sr.Microphone() as source:
            r.energy_threshold = 700
            r.pause_threshold = 0.5
            audio = r.listen(source)
            try:
                demande = r.recognize_google(audio, language='fr-FR')
                print("L'utilisateur à dis : " + demande)
                ecoute = False
                return demande
            except Exception:
                pass
