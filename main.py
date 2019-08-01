import cv2
import sys
import numpy as np
import os 
import json
import time
import threading
import socket
import threading
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import parse_qs
import cgi
import base64
import io
from imageio import imread
import matplotlib.pyplot as plt
import json

from odes.odes import classfy
from FTTS import TTS
from news.news import NEWS
from news.read import READ
from ocr.ocr import OCR
from ocr.hau import HAU 
from ocr.pre import PRE
from sdes.imagecaption import CAPTION
from weather import WEATHER
from wiki import WIKI
from face.facedes import FACEDES
import cloudsight
from google.cloud import translate
from face.facerec import FACEREC
recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer.read('face/trainer/trainer.yml')
cascadePath = "face/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
info = []
names=[]
text=''
checkqr=0
qr=''
checkface=0
curpage=0
tintuc=[]
import vlc
    
with open('face/labels.txt', 'r',encoding='utf-8') as filehandle:  
    i=0
    info.append(('0','0'))
    for line in filehandle:
        currentPlace = line[:-1]
        names.append(currentPlace)
        if (i!=0):
            with open('face/contact/'+str(i)+'.json',encoding='utf-8') as f:
                        d = json.load(f)
            info.append((d["name"],d["phone"]))
        i=i+1
print('nap danh ba')
print (info)
print ('khoi chay bo xu ly')

def r(text):
    global curpage,tintuc
    if (text=='' or text=="stop" or text=="exitnews"):
        player.stop()
    elif (text[:4]=="news"):
        bao=""
        curpage=1
        chude=text[5:]
        bao=bao+(str("trang "+str(curpage)))+"."
        tintuc=NEWS(chude)
        for a,b,c in tintuc:
            if (int(a)+1<=(curpage*5) and int(a)+1>(curpage*5-5)):
                bao=bao+(str("bài số "+ str(a)+": "+b))+"."
        TTS(bao,0)
        return bao
    elif (text=="next"):
        bao=""
        curpage=curpage+1
        bao=bao+(str("trang "+str(curpage)))+"."
        print(tintuc)
        for a,b,c in tintuc:
            if (int(a)+1<=(curpage*5) and int(a)+1>(curpage*5-5)):
                bao=bao+(str("bài số "+ str(a)+": "+b))+"."
        TTS(bao,0)
        return bao
    elif (text=="pre"):
        bao=""
        curpage=curpage-1
        bao=bao+(str("trang "+str(curpage)))+"."
        for a,b,c in tintuc:
            if (int(a)+1<=(curpage*5) and int(a)+1>(curpage*5-5)):
                bao=bao+(str("bài số "+ str(a)+": "+b))+"."
        TTS(bao,0)
        return bao
    elif (text[:4]=="read"):
        ans=READ(str(tintuc[int(text[4:])-1][2]),0)
        TTS(ans,0)
        return ans
    elif (text[:4]=="rsum"):
        ans=READ(str(tintuc[int(text[4:])-1][2]),1)
        TTS(ans,0)
        return ans
    elif (text=='fash'):
    	ans=FASHION()
    	TTS(ans,1)
    	return ans
    elif (text=='rec'):
        kq=FACEREC()
        kqq=""
        for n in kq:
            if (n!='Unknown'):
                kqq=kqq+names[int(n)]+","
        if (kqq!=""):
            TTS(kqq,1)
            return(kqq)
        else:
        	pass
            #TTS("không có trong dữ liệu",1)
            #return ("không có trong dữ liệu")
        ans=classfy()
        TTS(ans,1)
        return ans
    elif (text=='facedes'):
        ans=FACEDES('all')
        TTS(ans,0)
        return ans
    elif (text=='facerec'):
        kq=FACEREC()
        kqq=""
        for n in kq:
            if (n!='Unknown'):
                kqq=kqq+names[int(n)]+","
        if (kqq!=""):
            TTS(kqq,1)
            return(kqq)
        else:
            TTS("không có trong dữ liệu",1)
            return ("không có trong dữ liệu")
    elif (text[:4]=='prof'):
        try:
            id=-1
            ok=False
            for name in names:
                id=id+1
                if (name==text[5:]):
                    TTS('tên: '+info[id][0]+'. điện thoại :'+info[id][1],0)
                    return ('tên: '+info[id][0]+'. điện thoại :'+info[id][1])
                    ok=True
                    break
            if (ok==False):
                TTS("không có trong dữ liệu",0)
                return ("không có trong dữ liệu")
        except:
            TTS("lỗi",0)
            reuturn ("lỗi")
    elif (text=='ocr'):
        ans=OCR()
        ans=HAU(ans)
        TTS(ans,0)
        return(ans)
    elif (text=="sdes"):
        ans=CAPTION()
        TTS(ans,0)
        return (ans)
    elif (text=='odes'):
        ans=classfy()
        TTS(ans,1)
        return ans
    elif (text[:4]=='wiki'):
        try:
            TTS(WIKI(text[5:]),0)
            return (WIKI(text[5:]))
        except:
            TTS("lỗi",1)
            return ("lỗi")
    elif (text[:7]=='weather'):
        try:
            ans=WEATHER(text[8:])
            TTS(ans,0)
            return ans
        except:
            ans=WEATHER("kon tum")
            TTS(ans,0)
            return ans
    elif (text[:5]=="music"):
        try:
            ans=GETMUSIC(text[6:])
            print(ans)
            player=vlc.MediaPlayer(ans)
            player.play()
        except:
            return("lỗi") 
    else:
        TTS("Không hiểu lệnh",0)
        return ("Không hiểu lệnh")
def decodeimg(data,re):
    dataa=data.encode()
    b64_string = dataa.decode()
    img = imread(io.BytesIO(base64.b64decode(b64_string)))
    cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    if (re=='ocr'):
        cv2_img=PRE(cv2_img)
    cv2.imwrite("image.jpg", cv2_img)
class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
    def do_GET(self):
        self._set_headers()
        print (self.path)
        print (parse_qs(self.path[2:]))
        self.wfile.write("Get Request Received!".encode())
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        re=(form.getvalue("text"))
        print(re)
        try:
            decodeimg(form.getvalue("img"),re)
        except:
            pass
        re=r(re)
        self.wfile.write(bytes(re,'utf-8'))
def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Server running at localhost:8088...')
    httpd.serve_forever()

run()
