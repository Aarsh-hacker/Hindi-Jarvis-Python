from distutils.log import error
import pyttsx3
import speech_recognition as sr
from requests import get
import pyautogui
import subprocess
import os
import smtplib
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
engine.setProperty("rate", 150)
chrome= '<<-chrome path->>'
def say(audio):
    engine.say(audio)
    engine.runAndWait()

def graphic():
    print("___________     _        _____                 --------   --------- ")
    print("     |         / \      |     |  \          /      |      |         ")
    print("     |        /   \     |     |   \        /       |      |         ")
    print("     |       /     \    |-----     \      /        |      --------  ")
    print("     |      /-------\   | \         \    /         |             |  ")
    print("     |     /         \  |  \         \  /          |             |  ")
    print("------    /           \ |   \         \/       ---------  --------  ")
    print("                                                                   © aarshverma")

def wishMe():
    say("नमस्ते sir") 
    say("मैं jarvis हूँ | मैं आपकी क्या सहायता कर सकती हूँ |")

def takeCommandenglish():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......wait a moment")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except:
        print("Please say that again........!")
        return "None"
    return query

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......wait a moment")
        query = r.recognize_google(audio, language='hi')
        print(f"User said : {query}\n")

    except:
        print("Please say that again........!")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<<-email-id---->', 'email-paasword')
    server.sendmail('<<-email-id---->', to, content)
    server.close()

def taskexecute():
    graphic()
    wishMe()
    while True:
        query = takeCommand()
         
        if 'हाल-चाल' in query:
            say("एकदम झकास sir!")

        elif 'क्या कर रही हो' in query:
            say("आपसे बात करने का इंतज़ार!")

        elif 'स्क्रीनशॉट' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            say('Screenshot ले लिया')

        elif 'क्रोम खोलो' in query:
            say("chrome खुल रहा है ")
            cPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cPath)
            say("chrome खुल गया")

        elif 'ईमेल' in query:
            try:
                say("email id type कीजिये")
                email_id=input()
                to = email_id
                say("मैं क्या भेजूँ?")
                content = takeCommand()
                say("email भेजी जा रही है ")
                sendEmail(to,content)
                say("email  भेजी जा चुकी है |")
                
            except:
                say("में ईमेल नहीं भेज पा रही हूँ", error)


        elif 'वेबसाइट खोलो' in query:
            say("कौन सी website खोलूँ sir उसका URL type कीजिये\n")
            website_name = input()
            webbrowser.get(chrome).open(website_name)
            say(f"आपकी website खुल गयी sir.")

        elif'आईपी एड्रेस' in query:
            ip = get('https://api.ipify.org').text
            print(f"आपका ip address है {ip}")
            say(f"आपका ip address है {ip} ")

taskexecute()