import pyttsx3 as p
import speech_recognition as sr
from selenium_web import Infow
from youtube_auto import YouTubeInfo
from news import NewsSearch
from jokes import*
import randfacts
import datetime

engine=p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voices',voices[1].id)
print(rate)

def speak(text):
    engine.say(text)
    engine.runAndWait()
today_date=datetime.datetime.now()
speak("today is,"+today_date.strftime("%d")+today_date.strftime("%B"))

r=sr.Recognizer()

speak("hello sunny, i am ur voice assistant,how are you?")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("i am a voice assistant, i can help you with any task")
speak("i am capable of ur tasks")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio=r.listen(source)
    text2=r.recognize_google(audio)
if "information" in text2:
    speak("you need info related to which topic")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio=r.listen(source)
        infor=r.recognize_google(audio)
    speak("searching in wikipedia".format(infor))
    print("searching in wikipedia".format(infor))
    assist = Infow()
    assist.get_info(infor) 
elif "play" and "video" in text2:
    speak("you want me to play which viddeo?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio=r.listen(source)
        vid=r.recognize_google(audio)
    speak("searching in wikipedia".format(vid))
    print("searching in wikipedia".format(vid))
    assist=YouTubeInfo()
    assist.search_video(vid)
    assist.keep_open()
elif "news"   in text2:
    speak("you want me to open which news")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio=r.listen(source)
        new=r.recognize_google(audio)
    speak("searching in wikipedia".format(new))
    print("searching in wikipedia".format(new))
    new1=NewsSearch()
    new1.search_news(new)
    new1.keep_open()

elif "joke" or "jokes" in text2:
    speak("here is a joke for you")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
elif "fact" or "facts" in text2:
    x=randfacts.getFact()
    print(x)
    speak("did you know that, "+x)



