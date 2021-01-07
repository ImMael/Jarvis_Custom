import json
import requests
from Fonctionnalites.speak import speak


def whatWeather():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Paris&lang=fr&units=metric&APPID=36a7954299258aa25bd9ba8ceb3ab077')
    # pprint(r.json())
    reponse = json.loads(r.text)
    city = reponse["name"]
    description = reponse["weather"][0]["description"]
    tempCurrent = int (reponse["main"]["temp"])
    tempMin = int (reponse["main"]["temp_min"])
    tempMax = int (reponse["main"]["temp_max"])
    speak(f"Le ciel est actuellement {description} avec une température de {tempCurrent} degré à {city}. Il fera {tempMin} degré au minimum et {tempMax} degré au maximum.")