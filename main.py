# JARVIS

import speech_recognition as sr
import pyttsx3
import webbrowser
import google.generativeai as genai

from config import Settings

settings = Settings()

# configure api key
genai.configure(api_key=settings.GEMINI_API_KEY)

# Initialize the Gemini model 
model = genai.GenerativeModel('gemini-2.0-flash')

# initializing them
r = sr.Recognizer()
engine = pyttsx3.init()

# speaking function
def speak(text): 
    engine.say(text)
    engine.runAndWait()

# open web links
def processCommands(command: str):
    if "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open google" in command:
        webbrowser.open("https://google.com")
    elif "open github" in command:
        webbrowser.open("https://github.com")
    else:
        response = model.generate_content(f"You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please for the query below\n{command}")
        speak(response.text)

print("To activate Jarvis say Jarvis and then your command.")
speak("Initializing Jarvis...")
while True: 
    print("Recognizing...")
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2)
        word = r.recognize_google(audio)
        print(word)
        if word.lower() == "jarvis":
            speak("yes")
            print("Wait...")
            with sr.Microphone() as source:
                print("Jarvis Active")
                print("Listening...")
                audio = r.listen(source, timeout=3)
                command = r.recognize_google(audio)
                print(command)
                if (command.lower() == "stop"):
                    break
                processCommands(command.lower())

    except Exception as e:
        print(f"Error: {e}")

speak("Thank you for using me.")