from textblob import TextBlob
from Fonctionnalites.speak import speak

def translate(phrase):
    lang_f = {"francais": "fr",
              "anglais": "en",
              "albanais": "sq",
              "allemand": "de",
              "espagnol": "es",
    }

    new_phrase = phrase.split("traduis ")
    language = new_phrase[1].split("en ")
    to_translate = TextBlob(language[0])
    lang = lang_f[language[1]]
    translated = to_translate.translate(to=lang)

    result = {
        "traduction": translated,
        "language": language
    }

    print(f'La traduction de {result["language"][0]} en {result["language"][1]} donne {result["traduction"]}')

    return result

def speak_translate(phrase):
    result = translate(phrase)
    speak(f'La traduction de {result["language"][0]} en {result["language"][1]} donne {result["traduction"]}')