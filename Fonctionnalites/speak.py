import pyttsx3


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)
    engine.say(audio)
    engine.runAndWait()


def repeat(question):
    repeatable = question.split("répète après moi")
    speak(repeatable)

def hello():
    speak('Bonjour, comment allez vous ?')