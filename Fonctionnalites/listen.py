import speech_recognition as sr


def ecouter():
    ecoute = True
    r = sr.Recognizer()
    print('En écoute')
    while ecoute:
        with sr.Microphone() as source:
            r.pause_threshold = 0.8
            audio = r.listen(source)
            try:
                demande = r.recognize_google(audio, language='fr-FR')
                print("L'utilisateur à dis : " + demande)
                ecoute = False
                return demande
            except Exception:
                pass
