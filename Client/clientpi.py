import base64
import io
import requests
import socket
from dich import DICH
import time 
#from ttsn import TTS
from stt import STT
#from gsearch.googlesearch import search
import threading
import urllib
from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import subprocess
camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(0.1)
server="http://"+socket.gethostbyname('nkc')+":8088"
iot="http://"+socket.gethostbyname('ESP_9FA82C')+"/"
print("[CONNECT]")
print(server)
print(iot)
print("=========================")
s=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def checkmic(): 
    test = subprocess.Popen(["arecord", "-l"], stdout=subprocess.PIPE)
    listdev = test.communicate()[0]
    listdevv=str(listdev)
    if (listdevv.find("USB PnP Sound Device")>=0):
        return True
    else:
        return False
def capture_high():
    camera.resolution = (1280,1080)
    camera.rotation = 90
    camera.capture('input.jpg')
def capture_low():
    camera.resolution = (600,600)
    camera.rotation = 90
    camera.capture('input.jpg')
def main():
    global s
    time.sleep(2)
    print("mic")
    while 1:
        #print('OK')
        #text=input()
        input_state = GPIO.input(17)
        if (input_state==1):
            if (checkmic()==False):
                return
            text=STT()
        else:
            continue
        #text=input()
        text=DICH(text)
        print (text)
        #=============img======
        if (text=="fash" or text=="scan" or text=="facerec" or text=="odes" or text=="sdes" or text=="facedes" or text=="orc"):
            if (text=="orc"):
                capture_high()
            else:
                capture_low()
            #capturee()
            filename = "input.jpg"
            with open(filename, "rb") as fid:
                data = fid.read()
            img = base64.b64encode(data)
        else:
            img=""
        #======================
        file={
            'text': text,
            'img': img
        }
        r = requests.post(server,file)
        result = r.text
        print(result)
        #TTS(result)
def main_w_mic():
    time.sleep(2)
    print("no mic")
    global s
    count=0
    long=10
    text=""
    while 1:
        #text=input()
        input_state = GPIO.input(17)
        if (input_state==1):
            if (checkmic()==True):
                return
            print(count)
            count=count+1
            continue
        else:
            if count==0:
                continue
            if (count<long/2):
                capture_low()
                text="rec"
            else:
                capture_high()
                text="orc"
            count=0
            filename = "input.jpg"
            with open(filename, "rb") as fid:
                data = fid.read()
            img = base64.b64encode(data)
            file={
                'text': text,
                'img': img
            }
            print("ok")
            r = requests.post(server,file)
            result = r.text
            print(result)
        #TTS(result)
while 1:
    if(checkmic()==True):
        main()
    elif(checkmic()==False):
        main_w_mic()


