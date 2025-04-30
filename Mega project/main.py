import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine= pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
     
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        
    
   



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:   
     # listen for the wake word 'Jarvis'
     # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
           print("Listening....")
           audio = r.listen(source,  timeout=2, phrase_time_limit=1)
        
        
        print("recognizing...")
        try:  
            with sr.Microphone() as source:
              print("Listening....")
              audio = r.listen(source,  timeout=2, phrase_time_limit=1)
         
            Word = r.recognize_google(audio)
            if(Word.lower() == "jarvis"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                  print("Jarvis Active....")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)
         
            
        
                processCommand(command)
       
        except Exception as e:
            print("error; {0}".format(e))
     