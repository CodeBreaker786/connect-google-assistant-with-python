import speech_recognition as sr
import pywhatkit
import datetime
import pyjokes
from schedule import get_lecture_info
from utils import questionAnswer
from questions_response import get_question_response
 
# engine.setProperty('rate',120)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
print(sr.Microphone.list_microphone_names())

 
r = sr.Recognizer()

def take_command():
    
    try:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print('listening...')
            command = r.listen(source)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                return command
    except:
      pass
    
def speak(text):
    t1 = gtts.gTTS("Welcome to javaTpoint")    

def run_alexa():
    command = take_command()
    if command is None:
        return
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        print('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
    # elif 'who is' in command:
    #     person = command.replace('who the heck is', '')
    #     info = wikipedia.summary(person, 1)
        # talk(info)
    elif 'date' in command:
        print('sorry, I have a headache')
    elif 'are you single' in command:
        print('I am in a relationship with wifi')
    elif 'joke' in command:
        print(pyjokes.get_joke())
    elif 'which lecture' in command:
        print(get_lecture_info())
    elif [val for key, val in questionAnswer.items() if key.lower() in command.lower() ]!=[]:
        print([val for key, val in questionAnswer.items() if key.lower() in command.lower() ][0])
    else:
     print("Not understand you please try again")
       
        


while True:
    run_alexa()