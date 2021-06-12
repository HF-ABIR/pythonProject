import speech_recognition as alx
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = alx.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with alx.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'search' in command:
        who = command.replace('search', '')
        also_who = wikipedia.summary(who, 1)
        print(also_who)
        talk(also_who)
    else:
        talk("sorry professor, i didn't understand will you please say the right command")


while True:
    run_alexa()

