import imaplib
import email
from news1 import nws
import pprint
from cryptography.fernet import Fernet
import sys
import subprocess
import time
from asyncore import loop
from syscontrols.brightness import brt
from syscontrols.vloume import vlm
from Mail.main import mail
from Weather.main import weather
from Flask_Document_Converter.converter import app
from password.reset import userkey
import psutil
import todo
from pkg_resources import declare_namespace
import cv2
from boltiot import Bolt
import json
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
from todo import todo
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.python.keras.models import load_model
from ctypes import cast, POINTER
import wmi
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui as pg
print("finished imports")

mode = 0
# bolt setup
api_key = '3693dec9-5fe0-4743-bb6f-275cbb821b0e'
device_id = 'BOLT13166757'
mybolt = Bolt(api_key, device_id)

lemmetizer = WordNetLemmatizer()

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    # return "%d:%02d:%02d" % (hh, mm, ss)
    return "%0dhours and %02d minutes" % (hh, mm)
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmetizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_wprds = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_wprds:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = None
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rete', 160)
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Task_Gui():
    os.system('python main.py')

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Afternoon!")

    else:
        speak("Good Evening!")

    speak("what do you want")


def takeCommand(md):
    # It takes microphone input from the user and returns string output
    if md == 1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 600
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query
    else:
        userinp = input("Command :")
        return userinp

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '')
    server.sendmail('', to, content)
    server.close()


if not mybolt.isAlive():
    speak("IOT device Offline")

def getsmart():
    intent = input("what intent does it belong to\n")
    num1 = int(input("Enter the number of patterns\n"))
    num2 = int(input("ENter the number of responses\n"))
    print("Enter some patterns\n")
    patterns = []
    responses = []
    for i in range(num1):
        pt = input(f"pattern{i}\n")
        patterns.append(pt)
    for i in range(num2):
        resp = input("Enter some responses\n")
        responses.append(resp)
    y = {
        "tag": intent,
        "patterns": patterns,
        "responses": responses,
        "context_set": ""
    }
    def write_json(new_data, filename='intents.json'):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data['intents'].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
    write_json(y)
    from training import mainfunc
    mainfunc()

# For first time running gets username password of mail and sets up user face recognition
def initialisation():
    import imaplib
    import email
    from cryptography.fernet import Fernet
    import sys
    # print("Setting Up face recognition")
    # from facerecog import sample_generator, module_trainer
    # print('after')
    # sample_generator.main()
    # print("training")
    # module_trainer.module_gen()
    # print("setting up mail credentials")
    mail_username = input("Enter mail username")
    mail_password = input("Enter mail passsword")
    key = Fernet.generate_key()
    password = bytes(mail_password, encoding='utf-8')
    r = Fernet(key)
    token = r.encrypt(password)
    file1 = open(r'Mail/username.txt', 'w')
    file1.write(mail_username)
    file2 = open(r'Mail/password.txt', 'wb')
    file2.write(token)
    file3 = open(r'Mail/keys.txt', 'wb')
    file3.write(key)
    file3.close()
    file2.close()
    file1.close()
    print(token)
    test1=r.decrypt(token)
    print(test1)
    
    imap_server = "imap.gmail.com"
    file1 = open(r'Mail/username.txt', 'r')
    file2 = open(r'Mail/password.txt', 'r')
    file3 = open(r'Mail/keys.txt', 'r')
    content_list1 = file1.readlines()
    content_list2 = file2.readlines()
    content_list3 = file3.readlines()
    username = content_list1[0]
    password = content_list2[0]
    keyfromfile = content_list3[0]
    print("Username", username)
    print("Password", password)
    keyfromfile = bytes(keyfromfile, encoding='utf-8')
    print(keyfromfile)
    print(type(keyfromfile))
    r = Fernet(keyfromfile)
    print('r---', r)
    print(type(r))
    password = bytes(password, encoding='utf-8')
    print(password)
    # key = Fernet.generate_key()
    # password = bytes(password, encoding='utf-8')
    # r = Fernet(key)
    # token = r.encrypt(password)
    # print(token)
    test1=r.decrypt(password)
    print(test1)
    mail  = imaplib.IMAP4_SSL('imap.gmail.com')
    (retcode, capabilities) = mail.login(username,test1.decode('utf-8'))
    mail.list()
    mail.select('inbox')

    n=0
    (retcode, messages) = mail.search(None, '(UNSEEN)')
    if retcode == 'OK':

        for num in messages[0].split() :
            print('Processing ')
            n=n+1
            typ, data = mail.fetch(num,'(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    original = email.message_from_bytes(data[0][1])

                    print (original['From'])
                    print (original['Subject'])
                    typ, data = mail.store(num,'+FLAGS','\\Seen')

    print(n)

if __name__ == "__main__":
    print("inside main main")
    # face recognition
    speak("Please show your Face")
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('facerecog/trainer/trainer.yml')   #load trained model
    cascadePath = "facerecog/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type
    access = 0

    id = 3 #number of persons you want to Recognize


    names = ['','Akhil', 'Arjun']  #names, leave first empty bcz counter starts from 0

    print("reachd cam")
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    print("activated Cam")
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight
    print("finished setting video frameheight")
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    T=30

    while T!=0 and access == 0:
        print("reached cam.read()")
        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image
            accuracy1 = accuracy
            print("id",id)
            # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy < 100):
                if round(100 - accuracy)>45:
                    access = 1
                else:
                    access = 0
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
            if round(100 - accuracy1)<45:
                id='unknown'
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  

        cv2.imshow('camera',img) 
        if access:
            speak('autentication success')
        else:
            print('denied')
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        T=T-1

    # Do a bit of cleanup
    cam.release()
    cv2.destroyAllWindows()


    if access == 0:
        speak("can't recognize your face, please enter the password")
        key = input("can't recognize your face, please enter the password :")
        if (key == userkey()):
            access=1
            print("autentication success")
            speak("autentication success")
        else:
            for i in range(2):
                speak("Error! re-enter your password")
                key1 = input("Error! re-enter your password :")
                if (key1 == userkey()):
                    speak("autentication success")
                    print("autentication success")
                    access=1
                    break
    if (access==0):
        speak("autentication failed")
        print("authentication failed")        


    if access:
        intents = json.loads(open('deeplearning/intents.json').read())
        #     reloading model, classes, words.pkl files
        words = pickle.load(open('deeplearning/words.pkl', 'rb'))
        classes = pickle.load(open('deeplearning/classes.pkl', 'rb'))
        model = load_model('deeplearning/chatbot_model.h5')

        # ints = [{'intent': 'greeting', 'probability': '0.95000'}]
        # res = get_response(ints, intents)
        # speak(res)
        # if mode == 1:

        while True:
            query = takeCommand(mode).lower()
            
            # code to play a song from youtube
            # if first word of user sentence is play then execute this code
            print(query.split())
            if query.split()[0] == "play":
                from selenium import webdriver
                from selenium.webdriver.common.by import By
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver.support.ui import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC
                driver = webdriver.Chrome()
                driver.maximize_window()
                wait = WebDriverWait(driver, 3)
                presence = EC.presence_of_element_located
                visible = EC.visibility_of_element_located

                # Navigate to url with video being appended to search_query
                title = query.split(' ', 1)[1]
                print(title)
                driver.get('https://www.youtube.com/results?search_query={}'.format(str(title)))

                # play the video
                wait.until(visible((By.ID, "video-title")))
                driver.find_element_by_id("video-title").click()
            else:
                print("entered else")
                ints = predict_class(query)
                print("ints", ints)
                # print("float[ints][0]", float(ints[0]['probability']))
                try:
                    print("Before if")
                    if float(ints[0]['probability']) < 0.60000 and query!= "none":
                        print("after if")
                        webbrowser.open("https://www.google.com/search?q="+query)
                        # speak("Not sure what you meant there")
                        # userwish = input("Do you want me to learn")
                        # if userwish == 'yes':
                        #     getsmart()
                        #     speak("trained new model")
                        #     intents = json.loads(open('intents.json').read())
                        #     #     reloading model, classes, words.pkl files
                        #     words = pickle.load(open('words.pkl', 'rb'))
                        #     classes = pickle.load(open('classes.pkl', 'rb'))
                        #     model = load_model('chatbot_model.h5')

                    else:
                        print("entered 2nd else")
                        res = get_response(ints, intents)
                        print("res",res)
                        speak(res)

                        userintent = ints[0]['intent']
                        if userintent == 'lon':
                            response = mybolt.digitalWrite('0', 'HIGH')
                            print(response)
                        elif userintent == 'loff':
                            response = mybolt.digitalWrite('0', 'LOW')
                        elif userintent == 'Youtube':
                            speak("Add a search term")
                            query = takeCommand(mode).lower()
                            webbrowser.open("https://www.youtube.com/results?search_query="+query)
                        elif userintent == 'google':
                            speak("Add a search term")
                            query = takeCommand(mode).lower()
                            webbrowser.open("https://www.google.com/search?q="+query)
                        # Logic for executing tasks based on query
                        elif userintent == 'stats':
                            devices = AudioUtilities.GetSpeakers()
                            interface = devices.Activate(
                                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                            battery = psutil.sensors_battery()
                            speak(f"Battery at {battery.percent}")
                            speak(f"You are good for{secs2hours(battery.secsleft)}")
                            volume = cast(interface, POINTER(IAudioEndpointVolume))
                            speak(f"Volume levels at{round(volume.GetMasterVolumeLevelScalar()*100)}")
                            speak(f"Screen Brightness at{wmi.WMI(namespace='wmi').WmiMonitorBrightness()[0].CurrentBrightness}")

                        elif userintent == 'brightness':
                            brt()
                        elif userintent == 'volume':
                            vlm()
                        elif userintent == "switch window":
                            pg.hotkey('alt','tab')
                        elif userintent == "show workspace":
                            pg.hotkey('win','tab')
                        elif userintent == 'launch':
                            speak("what apps do you want to launch")
                            apps=takeCommand(mode) #change it later
                            pg.press('win')
                            time.sleep(2)
                            pg.write(apps)
                            time.sleep(1)
                            pg.press('enter')

                        elif userintent == 'init':
                            key = input("Enter Master Password")
                            if key == userkey():
                                initialisation()
                            else:
                                print("denied")
                        elif userintent == 'converter':
                            print("converter else")
                            webbrowser.open("http://127.0.0.1:5000")
                            app.run()
                            
                            
                        elif 'wikipedia' in query:
                            speak('Searching Wikipedia...')
                            query = query.replace("wikipedia", "")
                            results = wikipedia.summary(query, sentences=2)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)
                                  
                        elif 'open youtube' in query:
                            webbrowser.open("youtube.com")

                        elif 'open google' in query:
                            webbrowser.open("google.com")

                        elif 'open stackoverflow' in query:
                            webbrowser.open("stackoverflow.com")

                        elif 'play music' in query:
                            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                            songs = os.listdir(music_dir)
                            print(songs)
                            os.startfile(os.path.join(music_dir, songs[0]))

                        elif 'the time' in query:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            speak(f"The time is {strTime}")

                        elif 'open code' in query:
                            codePath = ""
                            os.startfile(codePath)

                        elif 'to do' in query:
                            todo()
                        elif 'news' in query:
                            obj = nws()
                            news_res = obj.news()
                            speak('Todays Headlines are..')
                            for index, articles in enumerate(news_res):
                                pprint.pprint(articles['title'])
                                speak(articles['title'])
                                if index == len(news_res)-2:
                                    break
                            speak('These were the top headlines, Have a nice day')

                        elif 'mail' in query:
                            speak(mail())
                        elif 'weather' in query:
                            speak(weather())
                        
    
    
                except Exception as e:
                    print("eda exception",e)
                    if "list network" in query:
                        devices = subprocess.check_output(['netsh','wlan','show','network'])
                        devices = devices.decode('ascii')
                        devices= devices.replace("\r","")
                        print(devices)

