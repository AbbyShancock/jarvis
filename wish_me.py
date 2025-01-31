import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio 
import wikipedia
import webbrowser
import smtplib
import os
import requests

engine = pyttsx3.init()

def wish_me():
    """Greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I assist you today?")