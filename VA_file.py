import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import subprocess
import wikipediaapi


# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set a custom User-Agent for Wikipedia requests
headers = {
    'User-Agent': 'MyVoiceAssistant/1.0 (sayakd915@gmail.com)'
}

# Initialize Wikipedia API with custom headers
wiki_wiki = wikipediaapi.Wikipedia('en', headers=headers)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Recognition complete.")
    return audio

def recognize_audio(audio):
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not hear your request.")
        return ""
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return ""

def open_website(url):
    webbrowser.open(url)
    speak(f"Opening {url}")

def open_application(app_name):
    try:
        subprocess.Popen(app_name)
        speak(f"Opening {app_name}")
    except Exception as e:
        print(f"Error opening application: {e}")
        speak("Sorry, I couldn't open the application.")

def get_wikipedia_summary(query):
    page_py = wiki_wiki.page(query)
    if page_py.exists():
        summary = page_py.summary[:400]  # Limit the summary to the first 400 characters
        speak(f"Here is some information about {query}: {summary}")
    else:
        speak(f"Sorry, I couldn't find information about {query} on Wikipedia.")

def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    
    while True:
        audio = get_audio()
        query = recognize_audio(audio)

        print(f"Recognized Query: {query}")

        if "hello" in query:
            speak("Hi there! How can I assist you?")
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        elif "open website" in query:
            speak("Sure, which website would you like me to open?")
            website_query = recognize_audio(get_audio())
            open_website(f"https://www.{website_query}.com")
        elif "open application" in query:
            speak("Sure, which application would you like me to open?")
            app_query = recognize_audio(get_audio())
            open_application(app_query)
        elif "tell me about" in query:
            entity = query.split("tell me about")[1].strip()
            get_wikipedia_summary(entity)
        elif "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
