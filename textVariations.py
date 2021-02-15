from Fonctionnalites.calcul import calculate
from Fonctionnalites.time import whatTimeIsIt, whatDayToday
from Fonctionnalites.whatWeather import whatWeather, getCity
from Fonctionnalites.speak import repeat


def getVariations():

    variations = {
        'Bonjour': 'Bonjour, comment allez vous ?',
        'quelle heure': whatTimeIsIt,
        'quel jour': whatDayToday,
        'répète après moi': repeat,
        'météo': whatWeather,
        'calcul': calculate,
        'covit': cov
        'covid':
    }
    return variations
