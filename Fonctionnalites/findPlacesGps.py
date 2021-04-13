import googlemaps
from datetime import datetime
import apiKey
from Fonctionnalites.speak import speak
import Fonctionnalites.gpsTime

gmaps = googlemaps.Client(key=apiKey.getKey())


def getNearPlace(question):
    answer = question.split(" le")
    pos = gmaps.find_place(answer[1], "textquery", fields=["business_status", "geometry/location", "place_id"], language="fr-FR")  # Fonction pour trouver la "place" la plus proche en fonction du mot clé, du format de demande, de la langue et de quelques champs
    near_place = gmaps.reverse_geocode(pos["candidates"][0]["geometry"]["location"])  # Alterner entre Longitude/Latitude et Adresse
    found_address = near_place[2]["formatted_address"]
    print(found_address)
    speak(f'Le {answer[1]} le plus proche se trouve au {found_address}')  # Adresse approximative trouvée la plus proche