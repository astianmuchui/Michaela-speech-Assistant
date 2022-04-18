import speech_recognition as sr

import pyttsx3

import pywhatkit

import datetime

import wikipedia

import pyjokes


listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def talk(text):
    
    engine.say(text)
    
    engine.runAndWait()

info = wikipedia.summary(person,1)

print(info)

talk(info)

def take_command():
    
    try:
        
        with sr.Microphone() as source:
            
            print("Listening...........")
            
            voice = listener.listen(source)
            
            command = command.lower()
            
            if 'michaela' in command:
                command = command.replace('michaela','')
                print(command)
    except:
        pass
    return command
def run_michaela():
    command = take_command()
    print(command)
    #PLAY SONG ON YOUTUBE
    if 'play' in command:
        
        song = command.replace('play','')
        
        talk('playing'+ song + '...')
        
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is'+time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is','')
        info
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'are you single' in command:
        talk("I am in love with my builder")
    elif 'joke' in command:
        joke = pyjokes.get_jokes()
        talk(joke)
    else:
        talk("Couldn't quite get your Command. Please type again")

while True:
    run_michaela()
        
