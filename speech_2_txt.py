import pyttsx3
import speech_recognition as sr
from pyttsx3 import *
import datetime
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')
engine.setProperty('rate', 190)




speak("Speech To Text Converter")
print("Speech To Text Converter")
while True:
    def speak(text):
        engine.say(text)
        engine.runAndWait()


    def tc():
        a = sr.Recognizer()
        with sr.Microphone() as src:
            print("Listening>>")
            ad = a.listen(src)

        try:
            s = a.recognize_google(ad, language='ta-IN')
        except Exception as e:
            speak("Did not hear your voice ,Please Say That Again")
            print("Did not hear your voice ,Please Say That Again")
            return "None"
        return s


    def voices(s):
        if 'நிறுத்து' in s:
            print('Thank you')
            quit()
        else:
            print(s)
            print("say 'நிறுத்து' to exit")

    speak("Listening")
    us = tc().lower()
    ai = voices(us)