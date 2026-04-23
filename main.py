import sys
import os
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.speech_engine import speak, listen
from modules.weather import get_weather
from modules.news import get_news
from modules.wikipedia_search import search_wikipedia
from modules.reminder import set_reminder
from modules.system_tasks import open_website
from config import DEFAULT_CITY

speak("Hello Tanvi. I am your personal assistant. How can I help you?")

while True:

    command = listen()

    # Time Command
    if "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak("Current time is " + current_time)

    # Weather Command
    elif "weather" in command:
        speak("Which city?")
        time.sleep(1)

        city = listen()

        # wait until valid input comes
        while city == "":
            speak("I did not catch that. Please say the city again.")
            city = listen()

        result = get_weather(city)
        speak(result)

    # News Command
    elif "news" in command:
        headlines = get_news()
        for headline in headlines:
            speak(headline)

    # Wikipedia Command
    elif "wikipedia" in command:
        speak("What should I search?")
        query = listen()
        result = search_wikipedia(query)
        speak(result)

    # Reminder Command
    elif "remind me" in command:
        speak("After how many seconds?")
        seconds_text = listen()

        if seconds_text.isdigit():
            seconds = int(seconds_text)
            speak("What should I remind?")
            message = listen()
            reminder_text = set_reminder(seconds, message)
            speak(reminder_text)
        else:
            speak("Please say a valid number")

    # Open Website
    elif "open google" in command:
        speak(open_website("https://www.google.com"))

    # Exit Command
    elif "exit" in command or "stop" in command:
        speak("Goodbye Tanvi")
        break

    else:
        speak("Sorry, I did not understand.")