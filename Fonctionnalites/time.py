import datetime
from Fonctionnalites.speak import speak


def whatTimeIsIt():
    """
    Permet d'annoncer l'heure actuelle
    """
    date = datetime.datetime.now()
    speak(f'Il est : {date.hour} heure et {date.minute} minutes')


def whatDayToday():
    """
    Permet d'annoncer la date actuelle
    """
    fr_month = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre")
    date = datetime.datetime.now()
    mois = fr_month[date.month - 1]
    speak(f'Nous sommes le {date.day} {mois} {date.year}')