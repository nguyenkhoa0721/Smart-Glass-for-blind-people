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

print("[INFO] loading encodings + face detector...")
data = pickle.loads(open("/media/nk/Work/smartglass_cloud/facedeeplearning/1.pickle", "rb").read())

print("[INFO] starting video stream...")
vs = VideoStream(0).start()

fps = FPS().start()
while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=300)
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
	for ((top, right, bottom, left), name) in zip(boxes, names):
		cv2.rectangle(frame, (left, top), (right, bottom),
			(0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			0.75, (0, 255, 0), 2)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
