import pyttsx3

engine = pyttsx3.init('espeak')
engine.setProperty('voice', 'de+m6')
engine.setProperty("rate", 150)

text = "Hallo Alex und Kerstin. Verpisst euch wieder."
engine.say(text)
engine.runAndWait()

