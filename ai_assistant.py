from time import strftime
from unittest import result
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

randNo = random.randint(1, 5)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning kritika!")

    elif hour>12 and hour<18:
        speak("Good Afternoon kritika!") 

    else:
        speak("Good Evening Kritika!")
    
    speak("I am ritss. How may i help you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 350
        audio = r.listen(source)

    try:
        print("Recognizing please wait...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except  Exception as e:
        print(e)
        print("Can you please say that again...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
       # logic for executing task based on query
        if 'wikipedia' in query:
           speak("Searching Wikipedia...")
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("Acording t wikipedia")
           print(results)
           speak(results)

        elif 'open youtube' in query:
           speak("opening youtube...")
           webbrowser.open("youtube.com")
        

        elif 'open google' in query:
           speak("opening google...")
           webbrowser.open("google.com")
        
        elif 'open github' in query:
            speak("opening github...")
            webbrowser.open("github.com")

        elif 'open stackoverflow' in query:
           speak("opening stackoverflow...")
           webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'D:\My songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[randNo]))

        elif 'open code' in query:
            codePath = "C:\\Users\\Avita\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"kritiika, the time is {strTime} it's good time to start coding!")

        elif 'bye' in query:
            speak("Thankyou for spending time with me. Meet you soon...")
            break
        
      



