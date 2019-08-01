# -*- coding: utf8 -*-
import cv2
import numpy as np
import sys
import json
import os
import time
face_classifier = cv2.CascadeClassifier('/media/nk/Work/smartglass_cloud/facedeeplearning/haarcascade_frontalface_default.xml')

def face_extractor(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return None
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]
    return cropped_face
#them info
face_id = sum(1 for line in open('/media/nk/Work/smartglass_cloud/facedeeplearning/labels.txt',encoding='utf-8'))
print(face_id)
name = input('Tên: ')
phone = input('SÐT: ')

#luu info
info={"name":name,"phone":phone}
with open('/media/nk/Work/smartglass_cloud/facedeeplearning/contact/'+str(face_id)+'.json', 'a',encoding='utf-8') as f:
     json.dump(info, f, ensure_ascii=False)
with open('/media/nk/Work/smartglass_cloud/facedeeplearning/labels.txt', 'a', encoding='utf-8') as f:  
    f.write("%s\n" %name)     
