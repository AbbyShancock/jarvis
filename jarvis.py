
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio 
import wikipedia
import webbrowser
import smtplib
import os
import requests
from speak import speak
from wish_me import wish_me
from take_command import take_command
from tell_time import tell_time
from tell_date import tell_date
from search_wikipedia import search_wikipedia
from open_website import open_website
from send_email import send_email
from get_weather import get_weather
from take_screenshot import take_screenshot
from tell_joke import tell_joke

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command()

        if "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "wikipedia" in command:
            search_wikipedia(command.replace("wikipedia", ""))
        elif "open youtube" in command:
            open_website("youtube")
        elif "open google" in command:
            open_website("google")
        elif "send email" in command:
            speak("What should I say?")
            content = take_command()
            speak("Whom should I send it to?")
            recipient = input("Enter recipient email: ")  # Input for demo purposes
            send_email(recipient, content)
        elif "weather" in command:
            get_weather()
        elif "joke" in command:
            tell_joke()
        elif "screenshot" in command:
            take_screenshot()
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to do that yet.")

### **2. `secrets.py` - Email Credentials**
#Create this file in the same directory as `jarvis.py` and store your email credentials securely.



#**Important:** Do not share this file. Use environment variables or encryption for security.







