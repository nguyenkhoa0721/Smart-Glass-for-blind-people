# -*- coding: utf8 -*-
import cv2
import numpy as np
import sys
import json
import os
import time
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return None
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]
    return cropped_face
#them info
face_id = sum(1 for line in open('labels.txt',encoding='utf-8'))
print(face_id)
name = input('Tên: ')
phone = input('SÐT: ')

#luu info
info={"name":name,"phone":phone}
with open('contact/'+str(face_id)+'.json', 'a',encoding='utf-8') as f:
     json.dump(info, f, ensure_ascii=False)
with open('labels.txt', 'a', encoding='utf-8') as f:  
    f.write("%s\n" %name)
print("\nLook the camera and wait ...")


# luu hinh
cap = cv2.VideoCapture(0)
count = 0
os.makedirs('dataset/' + str(face_id))
while True:
    print(count)
    ret, frame = cap.read()
    cv2.imshow('Face', frame)
    if face_extractor(frame) is not None:
        count += 1
        if count%20==0:
        	file_name_path = "dataset/" + str(face_id) + '/' + str(count) + ".jpg"
        	cv2.imwrite(file_name_path, frame)
        #time.sleep(0.2)
    else:
        print("Face not found")
        pass
    if cv2.waitKey(1) == 13 or count == 300: 
        break
            
cap.release()
cv2.destroyAllWindows()      
print("Complete")
