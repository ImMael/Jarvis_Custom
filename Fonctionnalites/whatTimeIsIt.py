import datetime
from Fonctionnalites.speak import speak


def whatTimeIsIt():
    date = datetime.datetime.now()
    speak(f'Il est : {date.hour} heure et {date.minute} minutes')