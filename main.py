
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
    r = sr.Recognizer()
    with sr.Microphone(device_index=3) as source:
        print('En écoute')
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            Demande = r.recognize_google(audio,language='fr-FR')
            print("L'utilisateur à dis : " + Demande)
            # playsound('arouf-gangsta-begaye.wav')
        except Exception as er:
            print(er)
        try:
            return Demande
        except UnboundLocalError:
            pass


fr_month = ("Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre")

def repondre():
    # speak("Bonjour, que puis-je pour vous ?")
    question = ecouter()
    date = datetime.datetime.now()
    mois = fr_month[date.month - 1]
    if "bonjour" in question:
        speak('Bonjour, comment allez vous ?')
        repondre()
    elif "quelle heure est-il" in question:
        speak(f'Il est : {date.hour} heure et {date.minute} minutes')
    elif "on est quel jour" in question:
        speak(f'Nous sommes le {date.day} {mois} {date.year}')
    elif "répète après moi" in question:
        repeatable = question.split("répète après moi")
        speak(repeatable)
    else:
        playsound('arouf-gangsta-begaye.wav')


if __name__ == '__main__':
    while(True):
        try:
            appel = ecouter()
            if "Jarvis" in appel:
                speak('Bonjour, je vous écoute')
                repondre()
        except TypeError:
            pass

