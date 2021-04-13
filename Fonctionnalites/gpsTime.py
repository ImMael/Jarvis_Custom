import googlemaps
from datetime import datetime
import apiKey
from Fonctionnalites.speak import speak
from prettyprinter import pprint


gmaps = googlemaps.Client(key=apiKey.getKey())

def getTravelTime(question):
    print('YOOO')
    places = question.split(" au")
    place = places[1].split(" depuis")


    SRC = place[0]
    DEST = place[1]
    now = datetime.now()

    if "voiture" in question:
        directions_result = gmaps.directions(SRC, DEST, mode="driving", departure_time=now)
        # pprint(gmaps.directions(SRC, DEST[1], mode="", departure_time=now))
        time = directions_result[0]["legs"][0]["duration_in_traffic"]["text"] # Pour récupérer le temps
        adress = directions_result[0]["legs"][0]["distance"]["text"]  # Distance
        time = time.replace("hour","heure")
        time = time.replace("mins", "minutes")
        speak(f'Pour aller au {DEST[1]} il vous faudra {time} et faire {adress}')
    elif "à pied" in question:
        directions_result = gmaps.directions(SRC, DEST, mode="walking", departure_time=now)
        time = directions_result[0]["legs"][0]["duration"]["text"]  # Pour récupérer le temps
        adress = directions_result[0]["legs"][0]["distance"]["text"]  # Distance
        time = time.replace("hour", "heure")
        time = time.replace("mins", "minutes")
        speak(f'Pour aller au {DEST} il vous faudra {time} et faire {adress}')
    elif " vélo" in question:
        directions_result = gmaps.directions(SRC, DEST, mode="bicycling", departure_time=now)
        pprint(gmaps.directions(SRC, DEST, mode="bicycling", departure_time=now))
        time = directions_result[0]["legs"][0]["duration"]["text"]  # Pour récupérer le temps
        adress = directions_result[0]["legs"][0]["distance"]["text"]  # Distance
        time = time.replace("hour", "heure")
        time = time.replace("mins", "minutes")
        speak(f'Pour aller au {DEST} il vous faudra {time} et faire {adress}')
    elif " transport" in question:
        directions_result = gmaps.directions(SRC, DEST, mode="transit", departure_time=now)
        # pprint(gmaps.directions(SRC, DEST, mode="transit", departure_time=now))
        # pprint(directions_result[0]["legs"][0])
        time = directions_result[0]["legs"][0]["duration"]["text"]  # Pour récupérer le temps
        adress = directions_result[0]["legs"][0]["distance"]["text"]  # Distance
        departure = directions_result[0]["legs"][0]["departure_time"]["text"]   # heure de départ
        arrival = directions_result[0]["legs"][0]["arrival_time"]["text"]   # heure d'arriver
        time = time.replace("hour", "heure")
        time = time.replace("mins", "minutes")
        speak(f'Pour aller au {DEST} il vous faudra {time}, partir à {departure} pour arriver à {arrival}')
