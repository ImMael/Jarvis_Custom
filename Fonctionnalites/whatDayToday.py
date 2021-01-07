import datetime
from Fonctionnalites.speak import speak


def whatDayToday():
    fr_month = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre")
    date = datetime.datetime.now()
    mois = fr_month[date.month - 1]
    speak(f'Nous sommes le {date.day} {mois} {date.year}')