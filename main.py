import speech_recognition as sr
import pywhatkit
import datetime
import pyjokes
from schedule import get_lecture_info
from utils import questionAnswer
from questions_response import get_question_response
import gtts  
from playsound import playsound  
print(sr.Microphone.list_microphone_names())

 
r = sr.Recognizer()

def take_command():
    try:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print('listening...')
            audio_text = r.listen(source)
            command=r.recognize_google(audio_text)
            command = command.lower()
            print(command)
            if 'future' in command:
                command = command.replace('future','')
                return command
    except:
      pass
    

def speak(text):
    t1 = gtts.gTTS(text)
    t1.save("sound.mp3")  
    playsound("sound.mp3")  
      
    
    
    
    
def run_alexa():
    command = take_command()
    if command is None:
        return
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    # elif 'who is' in command:
    #     person = command.replace('who the heck is', '')
    #     info = wikipedia.summary(person, 1)
        # talk(info)
    elif 'date' in command:
        speak('sorry, I have a headache')
    elif 'are you single' in command:
        speak('I am in a relationship with wifi')
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'which lecture' in command:
        speak(get_lecture_info())
    elif [val for key, val in questionAnswer.items() if key.lower() in command.lower() ]!=[]:
        speak([val for key, val in questionAnswer.items() if key.lower() in command.lower() ][0])
    else:
     speak("Not understand you please try again")
       
        


while True:
    run_alexa()