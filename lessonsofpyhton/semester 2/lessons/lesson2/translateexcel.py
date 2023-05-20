import pandas as pd
from googletrans import Translator

text = pd.read_excel("semester 2/googletranselessons/Grades.xlsx")


a = Translator.translate(text=text, src="en", dest="uk")
print(a.text)
