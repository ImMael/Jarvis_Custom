from Fonctionnalites.calcul import calculate
from Fonctionnalites.time import whatTimeIsIt, whatDayToday
from Fonctionnalites.whatWeather import whatWeather
from Fonctionnalites.speak import repeat, hello
from Fonctionnalites.disease import covcases
from Fonctionnalites.translate import speak_translate
from Fonctionnalites.memo import memo


def getVariations():

    variations = {
        'Bonjour': hello,
        'quelle heure': whatTimeIsIt,
        'quel jour': whatDayToday,
        'répète après moi': repeat,
        'météo': whatWeather,
        'calcul': calculate,
        'covit': covcases,
        'covid': covcases,
        'traduis ': speak_translate,
        'rappelle-moi': memo,
    }
    return variations
