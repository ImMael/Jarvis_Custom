from Fonctionnalites.calcul import calculate
from Fonctionnalites.time import whatTimeIsIt, whatDayToday
from Fonctionnalites.whatWeather import whatWeather
from Fonctionnalites.speak import repeat, hello
from Fonctionnalites.disease import covcases
from Fonctionnalites.translate import speak_translate
from Fonctionnalites.memo import memo

# Liste de toutes les variations possible de demandes utilisateur
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
}

def getVariations():
<<<<<<< HEAD

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
=======
    """
    Récupère la totalité des variations de demandes utilisateur
    :return: un dictionnaire avec toutes les variations possible
    """
>>>>>>> a40ac2639d4120eb0fab5a37e68f3382af507dfc
    return variations
