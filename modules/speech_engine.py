import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-in")
        print("You said:", command)
        return command.lower()
    
    except sr.UnknownValueError:
        return ""

