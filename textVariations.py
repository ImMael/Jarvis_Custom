from Fonctionnalites.calcul import calculate
from Fonctionnalites.shoppingList import addShoppingList, deleteItemShoppingList, removeShoppingList
from Fonctionnalites.test import getStoreToProximity
from Fonctionnalites.time import whatTimeIsIt, whatDayToday
from Fonctionnalites.whatWeather import whatWeather
from Fonctionnalites.speak import repeat, hello
from Fonctionnalites.disease import covcases
from Fonctionnalites.translate import speak_translate
from Fonctionnalites.memo import memo

def getVariations():
    """
    Récupère la totalité des variations de demandes utilisateur
    :return: un dictionnaire avec toutes les variations possible
    """

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
        'rappelle-moi': memo,
        'ajoute à la liste de courses': addShoppingList,
        'supprime de la liste de courses': deleteItemShoppingList,
        'vider la liste de courses': removeShoppingList,
        # 'magasins à proximité': getStoreToProximity,
    }

    return variations
