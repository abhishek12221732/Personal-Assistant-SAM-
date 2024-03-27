import datetime
import wikipedia
import webbrowser
import pyttsx3
import subprocess
import pandas as pd
import os



################################################## PREREQUISITES ##################################################

######CONFIGURING VOICE

engine=pyttsx3.init()
voices=engine.getProperty('voices')
rate=engine.getProperty('rate')
engine.setProperty('rate',200)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()    


######CONGIGURING TIME AND WISHING

a=datetime.datetime.now()
hour=a.hour
minute=a.minute
second=a.second

######CODE TO WISH ONLY ONCE IN A DAY

df=pd.read_csv('a.csv')
nt_tm=df.iloc[0,0]
cr_tm=hour

if cr_tm < nt_tm:
    df=df.replace(nt_tm , cr_tm)
    df.to_csv('a.csv',index=False)
    
    if hour>=0 and hour<12:
        print('Good Morning Sir , I am Sam')
        speak("Good Morning Sir , I am Sam")
        print()
    elif hour>=12 and hour<18:
        print('Good Afternoon Sir , I am Sam')
        speak('Good Afternoon Sir , I am Sam')
        print()
    else:
        print('Good Evening Sir , I am Sam')
        speak('Good Evening Sir , I am Sam')
        print()
    
else:
    df=df.replace(nt_tm,cr_tm)
    df.to_csv('a.csv',index=False)


#############



###### FILE PATHS

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
calculator_path = 'C:\Windows\System32\calc.exe'
wmplayer = 'C:\Program Files (x86)\Windows Media Player\wmplayer.exe'
control_path = 'C:\Windows\System32\control.exe'
explorer = 'C:\Windows\explorer.exe'
mspaint = 'C:\Windows\System32\mspaint.exe'

################################################## MAIN LOGIC ##################################################
	
print("How may I help you ? :")
speak("How may I help you ? :")
print()


q=input(">>>")
q1=q.lower()

if "time" in q1:
    a=datetime.datetime.now()
    hour=a.hour
    minute=a.minute
    second=a.second
    
    if hour>=12:
       if hour>12:
        hour=hour-12
       print()
       print('Right now the time is',hour,':',minute,"PM")
       speak('Right now, the time is')
       speak(hour)
       speak(minute) 
       speak("P.M.")
    else:
        print()
        print('Right now the time is',hour,':',minute,"AM")
        speak('Right now, the time is')
        speak(hour)
        speak(minute)
        speak("A.M.")
elif "date" in q1 and "today" in q1:
    print()
    print('Today the date is',a.day,":",a.month,":",a.year)
    speak('Today the date is')
    speak(a.day)
    speak(a.month)
    speak(a.year)



################################################## BROWSER FUNCTIONS ##################################################
elif 'open google' in q1.lower():
    webbrowser.get(chrome_path).open('google.com')
elif 'open youtube' in q1.lower():
    webbrowser.get(chrome_path).open('youtube.com')
elif 'give' and 'news' in q1:
    webbrowser.get(chrome_path).open('bbc.com')
elif 'weather forecast' in q1:
    webbrowser.get(chrome_path).open('accuweather.com')
elif 'open flipkart' in q1:
    webbrowser.get(chrome_path).open('flipkart.com')
elif 'open amazon' in q1:
    webbrowser.get(chrome_path).open('amazon.in')
elif 'open whatsapp' in q1:
    webbrowser.get(chrome_path).open('web.whatsapp.com')
elif 'open facebook' in q1:
    webbrowser.get(chrome_path).open('facebook.com')
elif 'translate' in q1:
    webbrowser.get(chrome_path).open('translate.google.com')

################################################## APPLICATION FUNCTIONS ##################################################
elif 'open calculator' in q1:
    subprocess.call(calculator_path)
elif 'play music' in q1:
    subprocess.call(wmplayer)
elif 'open control panel' in q1:
    subprocess.call(control_path)
elif 'open chrome' in q1:
    subprocess.call(chrome_path)
elif 'open file explorer' in q1:
    subprocess.call(explorer)
elif 'open paint' in q1:
    subprocess.call(mspaint)
elif 'open windows media player' in q1:
    subprocess.call(wmplayer)
elif 'open media player' in q1:
    subprocess.call(wmplayer)
elif 'play a song' in q1:
    subprocess.call(wmplayer)


################################################## OTHER COMMON QUERIES ##################################################
elif 'what is your name' in q1:
    print()
    print("My name is Sam")
    speak("My name is Sam")

elif 'how can you help' in q1:
    print()
    print('I can open applications for you , websites , music player , do searches for you , and other simple stuff.')
    speak('I can open applications for you , websites , music player , do searches for you , and other simple stuff.')
elif 'what does your name means' in q1:
    print()
    print("Sir it means Simplified Assisting Machine ")
    speak("Sir it means Simplified Assisting Machine ")
elif 'what does you name mean' in q1:
    print()
    print("Sir it means Simplified Assisting Machine ")
    speak("Sir it means Simplified Assisting Machine ")
elif 'what is the meaning of you name' in q1:
    print()
    print("Sir it means Simplified Assisting Machine ")
    speak("Sir it means Simplified Assisting Machine ")

    

############################ WIKIPEDIA #####################
elif 'what is' in q1:
    print()
    print('searching.....')
    print()
    q1=q1.replace('what is',"")
    results=wikipedia.summary(q1,sentences=2)
    print(results)
    speak(results)

elif 'who is' in q1:
    print()
    print('searching.....')
    print()
    q1=q1.replace('who is',"")
    results=wikipedia.summary(q1,sentences=2)
    print(results)
    speak(results)

elif 'wikipedia' in q1:
    print()
    print('searching.....')
    print()
    q1=q1.replace('wikipedia',"")
    results=wikipedia.summary(q1,sentences=2)
    print(results)
    speak(results)

else:
    print()
    print("Sorry sir ! I could not understand")
    url1='https://www.google.com/search?q='
    url2=q1.replace(' ','+')
    speak("Sorry sir ! I could not understand")
    speak('but i can search it for you on google')
    webbrowser.get(chrome_path).open(url1+url2)

    
################################################## TO EXECUTE THE CODES AGAIN AFTER COMPLETION ##################################################




    
while True:
    print()
    q1=input('Anything else sir :').lower()
    if "time" in q1:
        a=datetime.datetime.now()
        hour=a.hour
        minute=a.minute
        second=a.second
    
        if hour>=12:
           if hour>12:
            hour=hour-12
           print()
           print('Right now the time is',hour,':',minute,"PM")
           speak('Right now, the time is')
           speak(hour)
           speak(minute) 
           speak("P.M.")
        else:
            print()
            print('Right now the time is',hour,':',minute,"AM")
            speak('Right now, the time is')
            speak(hour)
            speak(minute)
            speak("A.M.")
    elif 'date' in q1 and 'today' in q1:
        print()
        print('Today the date is',a.day,":",a.month,":",a.year)
        speak('Today the date is')
        speak(a.day)
        speak(a.month)
        speak(a.year)

    

##################################################  BROWSER FUNCTION ##################################################
    elif 'open google' in q1.lower():
        webbrowser.get(chrome_path).open('google.com')
    elif 'open youtube' in q1.lower():
        webbrowser.get(chrome_path).open('youtube.com')
    elif 'give' and 'news' in q1:
        webbrowser.get(chrome_path).open('bbc.com')
    elif 'weather forecast' in q1:
        webbrowser.get(chrome_path).open('accuweather.com')
    elif 'open flipkart' in q1:
        webbrowser.get(chrome_path).open('flipkart.com')
    elif 'open amazon' in q1:
        webbrowser.get(chrome_path).open('amazon.in')
    elif 'open whatsapp' in q1:
        webbrowser.get(chrome_path).open('web.whatsapp.com')
    elif 'open facebook' in q1:
        webbrowser.get(chrome_path).open('facebook.com')
    elif 'translate' in q1:
        webbrowser.get(chrome_path).open('translate.google.com')
    

    
################################################## APPLICATION FUNCTIONS ################################################## 
        
    elif 'open calculator' in q1:
        subprocess.call(calculator_path)
    elif 'play music' in q1:
        subprocess.call(wmplayer)
    elif 'open control panel' in q1:
        subprocess.call(control_path)
    elif 'open chrome' in q1:
        subprocess.call(chrome_path)
    elif 'open file explorer' in q1:
        subprocess.call(explorer)
    elif 'open paint' in q1:
        subprocess.call(mspaint)
    elif 'open windows media player' in q1:
        subprocess.call(wmplayer)
    elif 'open media player' in q1:
        subprocess.call(wmplayer)
    elif 'play a song' in q1:
        subprocess.call(wmplayer)

############################################ OTHER COMMON QUERIES #################################################
    elif 'what is your name' in q1:
        print()
        print("My name is Sam")
        speak("My name is Sam")

    elif 'how can you help' in q1:
        print()
        print('I can open applications for you , websites , music player , do searches for you , and other simple stuff.')
        speak('I can open applications for you , websites , music player , do searches for you , and other simple stuff.')
    elif 'what does your name means' in q1:
        print()
        print("Sir it means Simplified Assisting Machine ")
        speak("Sir it means Simplified Assisting Machine ")
    elif 'what does you name mean' in q1:
        print()
        print("Sir it means Simplified Assisting Machine ")
        speak("Sir it means Simplified Assisting Machine ")
    elif 'what is the meaning of you name' in q1:
        print()
        print("Sir it means Simplified Assisting Machine ")
        speak("Sir it means Simplified Assisting Machine ")

############### WIKIPEDIA #################
    elif 'what is' in q1:
        print()
        print('searching.....')
        print()
        q1=q1.replace('what is',"")
        results=wikipedia.summary(q1,sentences=2)
        print(results)
    elif 'who is' in q1:
        print()
        print('searching.....')
        print()
        q1=q1.replace('who is',"")
        results=wikipedia.summary(q1,sentences=2)
        print(results)
        speak(results)

    elif 'wikipedia' in q1:
        print()
        print('searching.....')
        print()
        q1=q1.replace('wikipedia',"")
        results=wikipedia.summary(q1,sentences=2)
        print(results)
        speak(results)
    elif q1=="no":
        print()
        print("Thank's for giving your time sir meet you next time.")
        speak("Thank's for giving your time sir , meet you next time.")
        break
    else:
        print()
        print('Sorry sir ! I could not understand')
        url1='https://www.google.com/search?q='
        url2=q1.replace(' ','+')
        speak('Sorry sir ! I could not understand')
        speak('but i can search it for you on google')
        webbrowser.get(chrome_path).open(url1+url2)
        



