import speech_recognition as sr
import pyttsx3
import os
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_app_or_website(command):
    command = command.lower()
    if "open" in command:
        item = command.replace("open", "").strip()

        # Handle websites
        if "." in item:  # e.g., "youtube.com"
            url = f"https://{item}"
            webbrowser.open(url)
            speak(f"Opening {item}")
        
        # Handle common desktop apps
        elif "notepad" in item:
            os.system("start notepad")
            speak("Opening Notepad")
        elif "calculator" in item or "calc" in item:
            os.system("start calc")
            speak("Opening Calculator")
        elif "chrome" in item:
            os.system("start chrome")
            speak("Opening Chrome")
        else:
            speak("I don't recognize that app.")
    else:
        speak("Please say 'open' followed by an app or website.")

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            open_app_or_website(command)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Could not request results.")

if __name__ == "__main__":
    speak("Jarvis is running in the background.")
    while True:
        listen_for_command()
