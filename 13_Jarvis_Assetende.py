import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import os
from gtts import gTTS
import pywhatkit as kit
import pygame
import sounddevice
from scipy.io.wavfile import write
import pyperclip
import pyautogui
import time
import requests
import sys
from googleapiclient.discovery import build
#-----------------------------------------
engen = pyttsx3.init()
def speak_old(text):
    engen.say(text)
    engen.runAndWait()
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

#-----------------------------------------
def Ai(me): 
        API_KEY = 'RhXPlNmcjL2BeHMaTNl7OOQwLU5dcOwb'  # Apni API Key yahan paste karo

        url = "https://api.ai21.com/studio/v1/j2-large/complete"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        # Clear aur simple prompt try karo
        data = {
            "prompt": me,
            "maxTokens": 50
        }

        response = requests.post(url, json=data, headers=headers)
        output = response.json()
        speaker = output['completions'][0]['data']['text']
        print(speaker)
        speak_old(speaker)
#------------------------------------------------------

def recognizer():
            recoding = sr.Recognizer()
            while True:
                try:
                    with sr.Microphone() as so:
                        print("listening.....")
                        recoding.adjust_for_ambient_noise(so)
                        audio = recoding.listen(so)
                        print("Recognizing....")
                        date = recoding.recognize_google(audio)
                        print(date)
                    if (date.lower()=="jarvis"):
                        speak_old("yes")
                        with sr.Microphone() as so:
                            print("jarvis active....")
                            recoding.adjust_for_ambient_noise(so)
                            audio = recoding.listen(so)
                        print("Recognizing....")
                        command = recoding.recognize_google(audio)
                        procommand(command)
                except sr.UnknownValueError:
                    print(" Not Understand ")
#------------------------
sec = 0
def jarvis_voice():
    recoding = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as so:
                print("tell number.....")
                recoding.adjust_for_ambient_noise(so)
                audio = recoding.listen(so)
                print("Recognizing....")
                jarvis_com = recoding.recognize_google(audio)
                jar = int(jarvis_com)
                sec = jar
                if sec == jar:
                    print("\nThanks")
                    break
                print(jarvis_com)
        except sr.UnknownValueError:
            print("No Numbers!")
#-----------------------------
# jarvis char
def jarvis_chat():
    recoding = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as so:
                print("chating.....")
                recoding.adjust_for_ambient_noise(so)
                audio = recoding.listen(so)
                print("Recognizing....")
                jarvis_com = recoding.recognize_google(audio)
                pyperclip.copy(jarvis_com)
                # pyautogui.click(636, 702)
                pyautogui.click(610, 666)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)
                pyautogui.press("enter")
                print(jarvis_com)
                if jarvis_com == "jarvis break":
                    speak_old("ok sir. chating break")
                    break
        except sr.UnknownValueError:
            print("No Numbers!")
#------------------------------
# recode
def recode(sec,name):
    print("Recoding Start........")
    rec = sounddevice.rec((sec*44100),samplerate=44100,channels=2)
    sounddevice.wait()
    write(name,44100,rec)
    print("recoding in successfully")
    speak_old("Recoding is seccessfully save!")
def searching(name2,name):
            recoding = sr.Recognizer()
            while True:
                try:
                    with sr.Microphone() as so:
                        print(f"{name2}_{name}.....")
                        recoding.adjust_for_ambient_noise(so)
                        audio = recoding.listen(so)
                        print("Recognizing....")
                        date = recoding.recognize_google(audio)
                except sr.UnknownValueError:
                    print(" Not Understand ")
                else:
                    return date
#--------------------------------------
def jarvis_AI():
    recoding = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as so:
                print("Jarvis_Ai.....")
                recoding.adjust_for_ambient_noise(so)
                audio = recoding.listen(so)
                print("Recognizing....")
                jarvis_com = recoding.recognize_google(audio)
                if jarvis_com == "ok close":
                    return
                else:
                    Ai(jarvis_com)
        except sr.UnknownValueError:
            print("Error!")

def procommand(c):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    if "open youtube" in c.lower():
        wb.open("https://youtube.com")
    elif "open google" in c.lower():
        speak_old("can you search on google.")
        mc = searching("search","google")
        print(mc)
        wb.get(chrome_path).open(f"https://www.google.com/search?q={mc}")
        return
    elif "open facebook" in c.lower():
        wb.open("https://facebook.com")
    elif "voice recording on" in c.lower():
        speak_old("ok recode yor voice.")
        speak_old("tell you voice seconds?")
        jarvis_voice()
        recode(sec,"demo.wav")
    elif "play on youtube" in c.lower():
        speak_old("ok sir, please searching")
        new  = searching("search","Youtube").lower()
        kit.playonyt(f"{new}")
    elif "please chat" in c.lower():
        speak_old("ok chating friends")
        jarvis_chat()
    elif "close this" in c.lower():
        time.sleep(3)# Wait to ensure browser is in focus
        pyautogui.hotkey('ctrl', 'w')
    elif "ok jarvis by" in c.lower():
         speak_old("Ok thanks, byby, Mr Arbaz")
         sys.exit()
    elif "please on" in c.lower():
        speak_old("ok say to Ai?")
        jarvis_AI()
    else:
        speak_old("please say again?")
if __name__=="__main__":
    speak_old("hello im jarvis can i help you")
    recognizer()