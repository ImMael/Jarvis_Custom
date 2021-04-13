import pyttsx3


def speak(audio):
    """
    Permet à l'assistant vocal de parler
    :param audio: String contenant la phrase à dire
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Voix pour Windows [0] et voix pour Mac [38]
    selected_voice = voices[38]
    engine.setProperty('voice', selected_voice.id)

    engine.say(audio)
    engine.runAndWait()


def repeat(question):
    """
    Fonction permettant de répéter une phrase donné par l'utilisateur
    :param question: String contenant la phrase donné par l'utilisateur
    """
    repeatable = question.split("répète après moi")
    speak(repeatable[1])

def hello():
    """
    Fonction permettant à l'assistant vocal de dire bonjour
    """
    speak('Bonjour, comment allez vous ?')