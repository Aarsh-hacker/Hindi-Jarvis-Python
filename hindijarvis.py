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
chrome= 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
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
    server.login('aarshverma.2006@gmail.com', '13441344')
    server.sendmail('aarshverma.2006@gmail.com', to, content)
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

        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            say('Screenshot ले लिया')

        elif 'chrome खोलो' in query:
            say("chrome खुल रहा है ")
            cPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cPath)
            say("chrome खुल गया")

        elif 'open Scratch' in query:
            say("scratch खुल रहा है ")
            cPath = "C:\\Users\\Lenovo\\Desktop\\Scratch 3"
            os.startfile(cPath)
            say("scratch खुल गया")

        elif 'open word' in query:
            say("word खुल रहा है ")
            cPath = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.exe"
            os.startfile(cPath)
            say("word खुल गया")

        elif 'open powerpoint' in query:
            say("powerpoint खुल रहा है")
            cPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013"
            os.startfile(cPath)
            say("powerpoint खुल गया")

        elif 'open excel' in query:
            say(" excel खुल रहा है")
            cPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013"
            os.startfile(cPath)
            say("excel खुल गया")

        elif 'open whatsapp' in query:
            say(" whatsapp खुल रहा है")
            subprocess.Popen(["cmd", "/C", "start WhatsApp:"], shell=True)
            say("whatsaspp खुल गया")

        elif 'open calculator' in query:
            say(" calculator खुल रहा है")
            subprocess.Popen(["cmd", "/C", "start Calculator:"], shell=True)
            say("calculator खुल गया")

        elif 'पापा को ईमेल' in query:
            try:
                say("sir email हिन्दी में भेजूँ या english में")
                launguage = takeCommand()
                if 'english' in launguage:
                    say("मैं क्या भेजूँ sir english में बोलिए")
                    content =  takeCommandenglish()
                    say("Email भेजी जा रही है ")
                    to = "p.arya04@gmail.com"
                    sendEmail(to, content)
                    say("Email भेजी जा चुकी है")

                elif 'हिंदी ' in launguage:
                    say("मैं क्या भेजूँ sir")
                    content =  takeCommand()
                    say("Email भेजी जा रही है ")
                    to = "p.arya04@gmail.com"
                    sendEmail(to, content)
                    say("Email भेजी जा चुकी है")
                
                else:
                    say("आपने गलत भाषा चुनी है ")

            except:
                say("I am unable to send the email because an error occured")

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
