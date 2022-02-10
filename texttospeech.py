import pyttsx3

data = input("Ingresa una palabra\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()