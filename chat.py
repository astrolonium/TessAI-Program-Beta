import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Use the microphone as audio source
with sr.Microphone() as source:
    print("Please say your name.")
    audio = r.listen(source)

# Convert speech to text
try:
    name = r.recognize_google(audio)
    print(f"Hello, {name}!")
    engine.say(f"Hello, {name}!")
    engine.runAndWait()
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
