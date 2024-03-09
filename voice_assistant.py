import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyttsx3 as p3

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)#,phrase_time_limit=5)#sends the phrase to google for recognition and waits 1
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            #print(data)
            return data
        except sr.UnknownValueError:
            print(" not understanding")


def speechtx(x):
    engine = p3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id) #0 for male and 1 is for female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x) 
    engine.runAndWait()

speechtx("hello")
sptext()            



if __name__ == '__main__': 
    

    if sptext().lower() == "hi peter":
        #print("test")
        data1 = sptext().lower()

        if "your name" in data1:
            name = "my name is peter"
            speechtx(name)
        elif 'old are you' in data1:
            age = "i am 2 year old"
            speechtx(age)
        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif 'web' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif 'joke' in data1:
            joke_1 = pyjokes.get_joke(language="en",category="neutral")
            speechtx(joke_1)


    else:
        print("thanks")