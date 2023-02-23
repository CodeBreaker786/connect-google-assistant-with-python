import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from schedule import get_lecture_info
from utils import questionAnswer
from questions_response import get_question_response
listener = sr.Recognizer()
engine = pyttsx3.init()
# engine.setProperty('rate',120)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
print(sr.Microphone.list_microphone_names())

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    
    try:
        with sr.Microphone() as source:
            # listener.adjust_for_ambient_noise(source,duration=1)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                return command
    except:
      pass
    


def run_alexa():
    command = take_command()
    if command is None:
        return
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    # elif 'who is' in command:
    #     person = command.replace('who the heck is', '')
    #     info = wikipedia.summary(person, 1)
        # talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'which lecture' in command:
        talk(get_lecture_info())
    elif [val for key, val in questionAnswer.items() if key.lower() in command.lower() ]!=[]:
        talk([val for key, val in questionAnswer.items() if key.lower() in command.lower() ][0])
    else:
     talk("Not understand you please try again")
       
        


while True:
    run_alexa()