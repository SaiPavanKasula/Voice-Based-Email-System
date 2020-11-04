from gtts import gTTS
import speech_recognition as sr
import os
import datetime
import webbrowser
import smtplib
import playsound
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
import re
import requests,json
#from weather import Weather
def talkToMe(audio):
    print(audio)
    tts=gTTS(text=audio,lang='en')
    tts.save('wav.mp3')
    #tts.save('file.mp3')
    #os.system('mpg123 audio.mp3')
    os.system(' wav.mp3')

def myCommand():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("am ready for ur command")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        command=r.recognize_google(audio)
        print("u said "+command+'/n')

    except sr.UnknownValueError:
        assistant(myCommand())
    return command

def assistant(command):
    "if statements for executing commands"

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
           # url = 'https://www.' + domain
            url = 'https://www.youtube.com'

            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'what doing' in command:
        talkToMe('Just doing my thing')
    elif 'tell me' in command:
        query = input("Input your query:")
        talkToMe('query')
        webbrowser.open("https://google.com/search?q=%s" % query)
    elif 'search' in command:
        talkToMe('which page i should open')
        page=myCommand()
        webbrowser.open("https://google.com/search?q=%s" % page)

    elif 'jokes' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')
    elif 'date' in command:
        now = datetime.datetime.now()
        print(str(now))

    elif 'play song' in command:
        playsound.playsound(r'C:\Users\Personal\Music\songs\girlslikeu.mp3', True)
        playsound.playsound(r'C:\Users\Personal\Music\songs\song5.mp3', True)
        playsound.playsound(r'C:\Users\Personal\Music\songs\ninnukori.mp3', True)
    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'k' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('senders_mail id', 'senders_password')

            #send message
            mail.sendmail('k', 'receivers_email', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        else:
            talkToMe('I don\'t know what you mean!')


talkToMe('Hey, I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())