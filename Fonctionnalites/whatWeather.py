import json
import requests
from Fonctionnalites.speak import speak
from pprint import pprint


def whatWeather(question):
    """
    Permet d'effectuer une requete API afin de récupérer et annoncer les détails de la météo
    :param question: la demande de météo de l'utilisateur
    """
    # On récupère la ville dans laquelle effectuer la requete API
    city = getCity(question)
    # On effectue une premiere requete dans la ville pour avoir les infos meteo actuel
    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=fr&units=metric&APPID=36a7954299258aa25bd9ba8ceb3ab077')
    # pprint(r.json())
    # On stock les resultats de la requete
    reponse = json.loads(r.text)
    # On stock les coordoonées GPS de la ville pour avoir beaucoup + d'informations meteo
    lat = reponse["coord"]["lat"]
    long = reponse["coord"]["lon"]
    # On conatene si la ville est en plusieurs mots
    if "+" in city:
        city = city.replace("+", " ")
    # On effectue la 2eme requete pour recuperer les details precis de la meteo sur la journee complete
    r = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&lang=fr&units=metric&exclude=hourly,minutely,alerts&APPID=36a7954299258aa25bd9ba8ceb3ab077')
    # pprint(r.json())
    reponse = json.loads(r.text)
    # On stock les differentes informations necessaires à annoncer par l'assistant
    description = reponse["current"]["weather"][0]["description"]
    tempCurrent = int (reponse["current"]["temp"])
    tempMin = int (reponse["daily"][0]["temp"]["min"])
    tempMax = int (reponse["daily"][0]["temp"]["max"])

    speak(f"Le temps est actuellement {description} avec une température de {tempCurrent} degré à {city}. Il fera {tempMin} degré au minimum et {tempMax} degré au maximum.")


def getCity(question):
    """
    Permet de récupérer la ville demandé par l'utilisateur
    :param question: la demande de l'utilisateur
    :return: la ville dans laquelle effectuer la requete
    """
    city = ""
    split = question.split("à ")
    split = split[1].split(" ")

    for i in range(len(split)):
        if split[0][0] == split[0][0].upper():
            city += split[i]
            try:
                next = split[i + 1]
                if next[0][0] == next[0][0].upper():
                    city += "+"
                else:
                    break
            except IndexError:
                break
    return city