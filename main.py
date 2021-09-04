import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour<12:
        speak("Good Morning sir")
    if hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("I am doctor, how can I help you?")

def take_command():
    query = None
    while query is None:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            speak("ask me")
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en-uk')
            print(f"you said: {query}\n")

        except Exception:
            print("I didn't get it. Could you please say that again")
            speak("I didn't get it. Could you please say that again")
            query = None

        if 'wikipedia' in query:
            query = query.lower()
            speak("Alright... i am on it")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak(results)

        if 'youtube' in query:
            chrome_path ="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url = "https://www.youtube.com")

        elif 'timer' in query:
            speak("For how long do you wan to set?")
            while query2 is None:
                r2 = sr.Recognizer()
                with sr.Microphone() as source2:
                    print("Listening...")
                    speak("ask me")
                    audio2 = r2.listen(source)

                try:
                    print("Recognizing...")
                    query2 = r2.recognize_google(audio2, language='en-uk')
                    print(f"you said: {query2}\n")

                except Exception:
                    print("I didn't get it. Could you please say that again")
                    speak("I didn't get it. Could you please say that again")
                    query2 = None
            time1 = ""

            for i in query2:
                if i.isdigit():
                    time1 = time1 + i

            time2 = int(time1)

            if 'minutes' or 'minute' in query2:
                speak("ok, your time starts now")
                time.sleep(60*time2)
                speak("sir, the rime is up")

            elif 'seconds' or 'second' in query2:
                speak("ok, your time starts now")
                time.sleep(time2)
                speak("sir, the rime is up")

            else:
                speak("No timer was set")





        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")

        elif 'google' in query:
            speak("Hello sir, what do you want to search?")
            query2 = None
            while query2 is None:
                r2 = sr.Recognizer()
                with sr.Microphone() as source2:
                    print("Listening...")
                    speak("ask me")
                    audio2 = r2.listen(source)

                try:
                    print("Recognizing...")
                    query2 = r2.recognize_google(audio2, language='en-uk')
                    print(f"you said: {query2}\n")

                except Exception:
                    print("I didn't get it. Could you please say that again")
                    speak("I didn't get it. Could you please say that again")
                    query2 = None
            query2 = query2.replace(" ","+")
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url="https://www.google.com/search?q="+query2+"&rlz=1C1AWFC_enIN871IN871&oq="+query2+"&aqs=chrome..69i57j35i39j0i433l2j46i433j0j46j0i433j0j46i10i433.3232j0j15&sourceid=chrome&ie=UTF-8")


def main():
    print("initializing doctor")
    wish_me()
    take_command()
main()