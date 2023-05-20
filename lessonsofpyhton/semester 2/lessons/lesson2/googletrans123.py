from googletrans import Translator

translator = Translator()

to_translate = "Hello World"
a = translator.translate(text=to_translate, src="en", dest="fr")

print(a.text)
