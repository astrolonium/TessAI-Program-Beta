import speech_recognition as sr
import pyttsx3
import os
import time


r = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def set_alarm(time_str):
    
    t = time.strptime(time_str, "%I:%M %p")
    sec = t.tm_hour * 3600 + t.tm_min * 60
    

    speak(f"Alarm set for {time_str}")
    while time.time() % 86400 != sec:
        pass
    speak("Time's up!")
    os.system("start alarm.wav")

def open_file(file_name):
    try:
        os.startfile(file_name)
        speak(f"Opening file {file_name}")
    except FileNotFoundError:
        speak(f"Sorry, I could not find file {file_name}")


with sr.Microphone() as source:
    print("Please say a command.")
    audio = r.listen(source)


try:
    command = r.recognize_google(audio)
    print(f"You said: {command}")
    if "set an alarm" in command:
        speak("What time would you like to set the alarm for?")
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            time_str = r.recognize_google(audio)
            set_alarm(time_str)
        except sr.UnknownValueError:
            speak("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            speak(f"Could not request results from Google Speech Recognition service; {e}")
    elif "open file" in command:
        file_name = command.split("open file ")[-1]
        open_file(file_name)
    else:
        speak("Sorry, I could not recognize that command.")
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
