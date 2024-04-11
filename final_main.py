from main import sign
import pyttsx3
import speech_recognition as sr
from pyttsx3 import *
import datetime
import requests

while True:
    print("Sign Language Recognition")
    print('1.Sign Language To Txt\n2.Speech To Text\n3.Exit')
    choice = input("Enter your choice:")
    if choice == '1':
        sign()
        break
    elif choice == '2':
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
    elif choice == '3':
        print('Thank you')
        break

