import speech_recognition as sr
import pyttsx3 as p

engine=p.init()
voices=engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
r=sr.Recognizer()

while(1):
    with sr.Microphone() as source:
        text = r.listen(source)

        try:
            recognized_text = r.recognize_google(text)
            print(recognized_text)
            if "weather" in recognized_text:
                engine.say("A sunny day is ahead of us.")
                engine.runAndWait()
            if "music" in recognized_text:
                engine.say("What kind of music are we thinking?")
                engine.runAndWait()
        except sr.UnknownValueError:
            print("Error!")
        except sr.RequestError as e:
            print("")
