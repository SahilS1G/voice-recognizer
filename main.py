import pyttsx3
import datetime
import pythonwin
import speech_recognition as sr 
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices)
# print(voices[1].id)

engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am cum sir. Please tell me how may I help you")
        
def takeCommand():
    #it takes microphone from the user and returns the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognize...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please")
        return ""
    
    return query
    

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
    
        #logic for executiong tasks based on query
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open spotify" in query:
            webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1E372StE2zt2fL")
            
        elif "open google" in query:
            webbrowser.open("www.google.com")
            
        elif "play music" in query:
            music_dr = "C:\\Users\\hp\\Music\\music"
            songs = os.listdir(music_dr)
            print(songs)
            os.startfile(os.path.join(music_dr,songs[0]))
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")     
            speak(f"Sir, the time is {strTime}")
            
        elif "open code" in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif "open whatsapp" in query:
            whatsappPath = "C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsappPath)
            
        elif "youtube search" in query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query[15::]}")   
            
        elif "google search" in query:
            webbrowser.open(f"https://www.google.com/search?client=firefox-b-d&q={query[14::]}")
            
        elif "spotify search" in query:
            webbrowser.open(f"https://open.spotify.com/search/{query[15::]}")
            
        
            
          
        
    

