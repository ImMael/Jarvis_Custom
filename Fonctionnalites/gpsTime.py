import googlemaps
from datetime import datetime
import apiKey
from Fonctionnalites.speak import speak


gmaps = googlemaps.Client(key=apiKey.getKey())

def getUserPosition():
    result = gmaps.geolocate()  # Fonction pour géolocaliser
    reverse_geocode_result = gmaps.reverse_geocode(result["location"])  # Alterner entre Longitude/Latitude et Adresse
    location = reverse_geocode_result[2]["formatted_address"]  # Avoir l'adresse dans le tableau de réponse renvoyée par la ligne au dessus
    return location  # Adresse géolocalisée approximative

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
    arrival = directions_result[0]["legs"][0]["arrival_time"]["text"]  # heure d'arrivée
    return departure, arrival


def replaceTime(time):
    time = time.replace("hour", "heure")
    time = time.replace("mins", "minutes")
    return time


def getTravelTime(question):
    places = question.split(" au")

    SRC = getUserPosition()
    DEST = places[1]

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
    if " transport" in question:
        result = getTime("transit", SRC, DEST)
        time = result[0]
        # adress = result[1]
        departure_and_arrival = get_departure_and_arrival(SRC, DEST)
        departure = departure_and_arrival[0]
        arrival = departure_and_arrival[1]

        time = replaceTime(time)
        speak(f'Pour aller au {DEST} il vous faudra {time}, partir à {departure} pour arriver à {arrival}')

