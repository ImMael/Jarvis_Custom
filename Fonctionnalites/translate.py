from textblob import TextBlob
from Fonctionnalites.speak import speak

def translate(phrase):
    lang_f = {" francais":"fr"," anglais":"en"," albanais":"sq"," allemand":"de"," espagnol":"es",}
    new_phrase = phrase.split("traduis")
    language = new_phrase[1].split("en")
    to_translate = TextBlob(language[0])
    lang = lang_f[language[1]]
    translated = to_translate.translate(to=lang)
    speak(f'{language[0]} en {language[1]} donne {translated}')