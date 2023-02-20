import speech_recognition as sr
from gtts import gTTS
import os

# Initialize speech recognition engine
r = sr.Recognizer()

# Use the microphone as audio source
with sr.Microphone() as source:
    print("Please read a story for me.")
    audio = r.listen(source)

# Convert speech to text
try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

# Convert text to speech and speak it out loud
tts = gTTS(text)
tts.save("output.mp3")
os.system("start output.mp3")
