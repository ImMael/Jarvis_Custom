import requests
from pprint import pprint

def getStoreToProximity(question):

    origins = "Poissy"
    destinations = "Paris"
    key = "AIzaSyDj4PwP4_TIzU5SGx4IzfgFBKPQJBhsTUM"

    r = requests.get(f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&key={key}')
    pprint(r.json())