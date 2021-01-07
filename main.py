<<<<<<< HEAD
from Fonctionnalites.answer import *
from Fonctionnalites.listen import ecouter
from Fonctionnalites.speak import speak


while True:
    appel = ecouter()
    if appel != None:
        try:
            if "Jarvis" in appel:
                speak('Bonjour, je vous écoute')
                repondre()
        except TypeError:
            pass
=======

import speech_recognition as sr
import pyttsx3
from playsound import playsound
import datetime
from Calcul import Calculate


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)
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
calcul = ("+", "-", "/", "x")

def repondre():
    # speak("Bonjour, que puis-je pour vous ?")
    question = ecouter()
    date = datetime.datetime.now()
    mois = fr_month[date.month - 1]
    if "Bonjour" in question:
        speak('Comment ça mon reuf ?')
    elif "quelle heure" in question:
        speak(f'Il est : {date.hour} heure et {date.minute} minutes')
    elif "quel jour" in question:
        speak(f'Nous sommes le {date.day} {mois} {date.year}')
    elif "répète après moi" in question:
        repeatable = question.split("répète après moi")
        speak(repeatable)
    elif ("+" in question) or ("-" in question) or ("x" in question) or ("/" in question):
        Calculate(question)
    else:
        playsound('arouf-gangsta-begaye.wav')


if __name__ == '__main__':
    while True:
        appel = ecouter()
        if appel != None:
            try:
                if "Jarvis" in appel:
                    speak('Oui ?')
                    repondre()
            except TypeError:
                pass
>>>>>>> walid
