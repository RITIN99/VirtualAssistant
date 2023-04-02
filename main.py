import speech_recognition as sr
import pywhatkit
import pyttsx3
import datetime
import wikipedia

list = sr.Recognizer()
mac = pyttsx3.init()

def talk(text):
    mac.say(text)

mac.runAndWait()

def input_inst():
    global inst
    try:
        with sr.Microphone() as origin:
            print('Say Something...')
            sp = list.listen(origin)
            inst = list.recognize_google(sp)
            inst = inst.lower()
            print(inst)
            if 'youtube' in inst:
                pywhatkit.playonyt(inst)
            else:
                pywhatkit.search(inst)

    except:
          pass

def pl_Va():

    inst = input_inst()
    print(inst)
    if "play" in inst:
        song = inst.replace('play',"")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in inst:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time' + time)
    elif 'date' in inst:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("today's date" + date)
    elif 'how are you' in inst:
        talk('i am fine,how about you')

    elif 'what is your name' in inst:
        talk('i am Va,what can i do for you?')

    elif 'who is' in inst:
        human = inst.replace('who is'," ")
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)

    else:
        talk('please repeat')

pl_Va()