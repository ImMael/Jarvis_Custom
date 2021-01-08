from covid import Covid
from Fonctionnalites.speak import speak

def covcases(country, asked):
    covid = Covid()
    #print(covid.list_countries())
    chosen = {"cas":"confirmed","morts":"deaths"}
    france = covid.get_status_by_country_name(country)
    speak(f'Il y a {france[chosen[asked]]} {asked} dû au covid en {country}')
