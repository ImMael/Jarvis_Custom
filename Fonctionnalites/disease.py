from covid import Covid
from Fonctionnalites.speak import speak

def covcases(question):
    covid = Covid()
    country = getCountry(question)
    #print(covid.list_countries())
    france = covid.get_status_by_country_name(country)
    speak(f'Il y a {france["confirmed"]} cas, et {france["death"]} morts dû au covid en {country}')


def getCountry(question):
    split = question.split("en")
    country = split[1]
    return country
