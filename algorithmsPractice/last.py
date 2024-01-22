import cowsay
import pyttsx3

engine= pyttsx3.init()
this= input('what is this')
cowsay.trex(this)
engine.say(this)
engine.runAndWait()