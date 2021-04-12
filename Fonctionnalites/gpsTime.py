import googlemaps
from datetime import datetime
import apiKey
from Fonctionnalites.speak import speak

gmaps = googlemaps.Client(key=apiKey.getKey())

def getTravelTime(question):
    SRC = "6 rue la fontaine 77230 Juilly"
    DEST = question.split(" au")
    now = datetime.now()
    directions_result = gmaps.directions(SRC, DEST[1], mode="driving", departure_time=now)
    time = directions_result[0]["legs"][0]["duration_in_traffic"]["text"] # Pour récupérer le temps
    adress = directions_result[0]["legs"][0]["distance"]["text"]  # Distance
    time = time.replace("hour","heure")
    time = time.replace("mins", "minutes")
    speak(f'Pour aller au {DEST[1]} il vous faudra {time} et faire {adress}')