import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import smtplib
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")

def speechtxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) #1 -> female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
#split the program and run only the specified program
    
    if "Hey Mark" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "My name is Mark"
                speechtxt(name)
            elif "How old are you" in data1:
                age = "I am 7 years old"
                speechtxt(age)  
            elif "What's the time" in data1:
                time = datetime.datetime.now() .strftime('%I%M%p')
                speechtxt(time)  
            elif "YouTube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "Joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtxt(joke_1)
            elif "Play music" in data1:
                 add = "D:\user\song"
                 listsong = os.listdir(add)
                 print(listsong)
                 os.startfile(os.path.join(add, listsong[0]))
            elif "exit" in data1:
                speechtxt("Thank u")
                break
            time.sleep(10)
    else:
        print("Thanks")

