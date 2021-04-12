from Fonctionnalites.calcul import calculate
from Fonctionnalites.shoppingList import addShoppingList, deleteItemShoppingList, removeShoppingList
from Fonctionnalites.test import getStoreToProximity
from Fonctionnalites.time import whatTimeIsIt, whatDayToday
from Fonctionnalites.whatWeather import whatWeather
from Fonctionnalites.speak import repeat, hello
from Fonctionnalites.disease import covcases
from Fonctionnalites.translate import speak_translate
from Fonctionnalites.memo import memo
from Fonctionnalites.gpsTime import getTravelTime

def getVariations():
    """
    Récupère la totalité des variations de demandes utilisateur
    :return: un dictionnaire avec toutes les variations possible
    """

    # Liste de toutes les variations possible de demandes utilisateur
    variations = {
        'Bonjour': hello,
        'Salut': hello,
        'Coucou': hello,

        'quelle heure': whatTimeIsIt,
        'donne-moi l\'heure': whatTimeIsIt,

        'quel jour': whatDayToday,
        'donne-moi la date': whatDayToday,

        'répète après moi': repeat,

        'météo': whatWeather,
        'quel temps fait-il': whatWeather,

        'calcul': calculate,
        'le résultat': calculate,

        'covit': covcases,
        'covid': covcases,

        'traduis ': speak_translate,

        'rappelle-moi': memo,

        'ajoute à la liste de courses': addShoppingList,
        'supprime de la liste de courses': deleteItemShoppingList,
        'vider la liste de courses': removeShoppingList,
        'vide la liste de courses': removeShoppingList,

        'Combien de temps': getTravelTime,

        # 'magasins à proximité': getStoreToProximity,
    }

    return variations