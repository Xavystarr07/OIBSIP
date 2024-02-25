import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio).lower()
            print(f"User: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't get that. Could you please repeat?")
            return ""
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")
            return ""

def execute_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()
        if command:
            execute_command(command)

