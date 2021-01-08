import json
import requests
from Fonctionnalites.speak import speak
from pprint import pprint


def whatWeather(question):
    city = getCity(question)
    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=fr&units=metric&APPID=36a7954299258aa25bd9ba8ceb3ab077')
    # pprint(r.json())
    reponse = json.loads(r.text)
    lat = reponse["coord"]["lat"]
    long = reponse["coord"]["lon"]
    if "+" in city:
        city = city.replace("+", " ")
    r = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&lang=fr&units=metric&exclude=hourly,minutely,alerts&APPID=36a7954299258aa25bd9ba8ceb3ab077')
    # pprint(r.json())
    reponse = json.loads(r.text)
    description = reponse["current"]["weather"][0]["description"]
    tempCurrent = int (reponse["current"]["temp"])
    tempMin = int (reponse["daily"][0]["temp"]["min"])
    tempMax = int (reponse["daily"][0]["temp"]["max"])
    print(f"Le temps est actuellement {description} avec une température de {tempCurrent} degré à {city}. Il fera {tempMin} degré au minimum et {tempMax} degré au maximum.")
    speak(f"Le temps est actuellement {description} avec une température de {tempCurrent} degré à {city}. Il fera {tempMin} degré au minimum et {tempMax} degré au maximum.")


def getCity(question):
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