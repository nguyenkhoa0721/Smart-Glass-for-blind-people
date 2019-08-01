# USAGE
# python pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2


data = pickle.loads(open("face/1.pickle", "rb").read())
def FACEREC():
	frame=cv2.imread('image.jpg')
	#frame = frame[:, :, ::-1]
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	
	boxes = face_recognition.face_locations(frame)
	encodings = face_recognition.face_encodings(rgb, boxes)
	names = []
	for encoding in encodings:
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"
		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1
			name = max(counts, key=counts.get)
		names.append(name)
	return names
#print(FACEREC())
