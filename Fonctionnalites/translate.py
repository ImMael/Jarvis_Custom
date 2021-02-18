from textblob import TextBlob
from Fonctionnalites.speak import speak


def translate(phrase):
    """
    Permet de traduire une phrase donné par l'utilisateur d'une langue vers une autre
    :param phrase: la phrase donné par l'utilisateur
    :return: un dictionnaire content la langue de traduction et la phrase traduite
    """
    lang_f = {"francais": "fr",
              "anglais": "en",
              "albanais": "sq",
              "allemand": "de",
              "espagnol": "es",
    }
    # on split pour récupérer ce que l'utilisateur veut traduire
    new_phrase = phrase.split("traduis ")
    # 2eme split pour récupérer la langue dans laquelle traduire
    language = new_phrase[1].split("en ")
    # On récupère uniquement la phrase à traduire
    to_translate = TextBlob(language[0])
    # On recupère le diminutif de la langue de traduction
    lang = lang_f[language[1]]
    # On effectue la traduction
    translated = to_translate.translate(to=lang)

    result = {
        "traduction": translated,
        "language": language
    }

    return result


def speak_translate(phrase):
    """
    Permet à l'assistant vocal d'annoncerla traduction oralement'
    :param phrase: phrase donné par l'utilisateur
    """
    result = translate(phrase)
    speak(f'La traduction de {result["language"][0]} en {result["language"][1]} donne {result["traduction"]}')