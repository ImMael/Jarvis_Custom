
import speech_recognition as sr
import pyttsx3
from playsound import playsound
import datetime


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


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


fr_month = ("Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre")

def repondre():
    # speak("Bonjour, que puis-je pour vous ?")
    question = ecouter()
    date = datetime.datetime.now()
    mois = fr_month[date.month - 1]
    if "Bonjour" in question:
        speak('Bonjour, comment allez vous ?')
    elif "quelle heure" in question:
        speak(f'Il est : {date.hour} heure et {date.minute} minutes')
    elif "quel jour" in question:
        speak(f'Nous sommes le {date.day} {mois} {date.year}')
    elif "répète après moi" in question:
        repeatable = question.split("répète après moi")
        speak(repeatable)
    else:
        playsound('arouf-gangsta-begaye.wav')


if __name__ == '__main__':
    while True:
        appel = ecouter()
        if appel != None:
            try:
                if "Jarvis" in appel:
                    speak('Bonjour, je vous écoute')
                    repondre()
            except TypeError:
                pass
