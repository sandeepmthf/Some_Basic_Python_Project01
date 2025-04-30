import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()  # Convert the command to lowercase for easier matching

    if "open" in command:
        # Extract the website name after "open"
        website = command.split("open", 1)[1].strip()  # Removes "open" and any spaces
        if website:
            # Check if the website contains 'http' or 'www'. If not, assume it's a common domain
            if not website.startswith("http://") and not website.startswith("https://"):
                website = "https://" + website .com
            
            webbrowser.open(website)  # Open the website in the default browser
            speak(f"Opening {website}")
        else:
            speak("Please specify the website after 'open'.")
    else:
        speak("Sorry, I didn't hear 'open'. Please say 'open' followed by a website name.")

if __name__ == "__main__":
    speak("Initializing assistant....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for command...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
