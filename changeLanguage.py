def languag(i):
    from googletrans import Translator, constants
    from pprint import pprint


    translator = Translator()
    translation = translator.translate(i, dest="en")
    # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    return translation.text