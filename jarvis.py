import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser as wb

engine = pyttsx3.init()  # to call the initial function
rate = engine.getProperty('rate')
engine.setProperty('rate', 135)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    now = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(now)
    print(now)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(f"Today's date is {day} of {month} {year}")
    print(f"{day}/{month}/{year}")


def wishme():
    speak("Hello Medha, Wellcome back")
    time()
    date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good morning Medha!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Medha!")
    elif hour >= 18 and hour < 24:
        speak("Good evening Medha!")
    else:
        speak("Good night Medha!")
    speak("Jarvis at your service, please let me know how can I help you")


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.record(source,duration=5)
        print(source)

    try:
        print("recognizing...")
        query = r.recognize(audio)
        print(f"you said {query}")
    except Exception as e:
        print(e)
        speak("I didn't quite understand, say that again please!")
        return "None"

    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "remember" in query:
            speak("What should I remember")
            data=takecommand()
            speak("You've asked me to remember"+data)
            remember=open('data.txt','a')
            remember.write(data)
            remember.close()

        elif "offline" in query:
            speak("glad to be of your service, take care")
            quit()
