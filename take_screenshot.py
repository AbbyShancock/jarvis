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

def take_screenshot():
    """Take a screenshot and save it."""
    screenshot_name = "screenshot.png"
    os.system(f"scrot {screenshot_name}")  # Works on Linux. Use `pyautogui.screenshot()` for Windows.
    speak("Screenshot taken successfully.")
