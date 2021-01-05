
import speech_recognition as sr
import pyttsx3
from playsound import playsound

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def ecouter():
    speak("Bonjour, que puis-je pour vous ?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('En écoute')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            Demande = r.recognize_google(audio,language='fr-FR')
            print('La commande est : ' + Demande)
            # playsound('arouf-gangsta-begaye.wav')
        except Exception as er:
            print(er)
        return Demande

def repondre():
    question = ecouter()
    if "salut mec" in question:
        print('Réponse en traitement')
        speak('Très bien et vous ?')
    else:
        playsound('arouf-gangsta-begaye.wav')


if __name__ == '__main__':
    repondre()


