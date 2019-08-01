import re
import urllib.request
from gtts import gTTS
import os
import playsound
import vlc,time
import keyboard
import cv2
def play(song):
	vlc_instance = vlc.Instance()
	player = vlc_instance.media_player_new()
	media  = vlc_instance.media_new(song)
	media.get_mrl()
	player.set_media(media)
	player.play()
	time_left = True
	while time_left == True:
	    song_time = player.get_state()
	    if str(song_time) != 'State.Opening' and str(song_time) != 'State.Playing':
	        time_left = False
	print ('Finished')
def create(text,title):
    tts = gTTS(text, lang='vi')
    tts.save('./TTSlib/'+title+".mp3")
    playsound.playsound('./TTSlib/'+title+'.mp3')
    return
def TTS(text,val):
    if val==1:
        if (os.path.isfile('./TTSlib/'+text+'.mp3')==True):
            playsound.playsound('./TTSlib/'+text+'.mp3')
        else:
        	create(text,text)
        	return
    else:
    	create(text,"audio")
    	return
#TTS("song.. giỏ bi. em có. khi ni. sóng bắt đầu từ gió. gió bắt đầu từ đâu?. em cũng không biết nữa. khi nào ta yêu nhau ",0)