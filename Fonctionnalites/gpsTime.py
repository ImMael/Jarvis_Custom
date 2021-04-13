import googlemaps
from datetime import datetime
import apiKey
from Fonctionnalites.speak import speak


gmaps = googlemaps.Client(key=apiKey.getKey())


def getTime(mobitity, SRC, DEST):
    now = datetime.now()
    directions_result = gmaps.directions(SRC, DEST, mode=mobitity, departure_time=now)
    if mobitity == "driving":
        time = directions_result[0]["legs"][0]["duration_in_traffic"]["text"]  # Pour récupérer le temps
    else:
        time = directions_result[0]["legs"][0]["duration"]["text"]  # Pour récupérer le temps
    adress = directions_result[0]["legs"][0]["distance"]["text"]  # Distance
    return time, adress


def get_departure_and_arrival(SRC, DEST):
    now = datetime.now()
    directions_result = gmaps.directions(SRC, DEST, mode="transit", departure_time=now)
    departure = directions_result[0]["legs"][0]["departure_time"]["text"]  # heure de départ
    arrival = directions_result[0]["legs"][0]["arrival_time"]["text"]  # heure d'arriver
    return departure, arrival


def replaceTime(time):
    time = time.replace("hour", "heure")
    time = time.replace("mins", "minutes")
    return time


def getTravelTime(question):
    places = question.split(" au")
    place = places[1].split(" depuis")

    SRC = place[0]
    DEST = place[1]

    if "voiture" in question:
        result = getTime("driving", SRC, DEST)
        time = result[0]
        adress = result[1]
        time = replaceTime(time)
        speak(f'Pour aller au {DEST} il vous faudra {time} et faire {adress}')
    elif "à pied" in question:
        result = getTime("walking", SRC, DEST)
        time = result[0]
        adress = result[1]
        time = replaceTime(time)
        speak(f'Pour aller au {DEST} il vous faudra {time} et faire {adress}')
    elif " vélo" in question:
        result = getTime("bicycling", SRC, DEST)
        time = result[0]
        adress = result[1]
        time = replaceTime(time)
        speak(f'Pour aller au {DEST} il vous faudra {time} et faire {adress}')
    elif " transport" in question:
        result = getTime("transit", SRC, DEST)
        time = result[0]
        # adress = result[1]
        departure_and_arrival = get_departure_and_arrival(SRC, DEST)
        departure = departure_and_arrival[0]
        arrival = departure_and_arrival[1]

        time = replaceTime(time)
        speak(f'Pour aller au {DEST} il vous faudra {time}, partir à {departure} pour arriver à {arrival}')
