import re
import urllib.request
import os
import playsound
import vlc,time
import keyboard
import cv2
from getaudio import GA
def play(song):
    playsound.playsound(song,True)
def create(text,title):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    string=[]
    for stuff in sentences:
        string.append(stuff)
    ans=""
    val=0
    for stringg in string:
        ans=ans+stringg
        val=val+1
        if (val%2==0):
            GA(ans,title)
            play('./TTSlib/'+title+'.mp3')
            ans=""
        else:
            pass
    if (len(string)%2!=0):
        GA(ans,title)
        play('./TTSlib/'+title+'.mp3')
def TTS(text,val):
    if val==1:
        if (os.path.isfile('./TTSlib/'+text+'.mp3')==True):
            play('./TTSlib/'+text+'.mp3')
        else:
        	create(text,text)
        	return
    else:
    	create(text,"audio")
    	return