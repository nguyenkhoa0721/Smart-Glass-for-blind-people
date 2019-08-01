from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images('/media/nk/Work/smartglass_cloud/facedeeplearning/dataset'))
knownEncodings = []
knownNames = []

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):

	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]
	
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	boxes = face_recognition.face_locations(rgb,
		model='hog')
	encodings = face_recognition.face_encodings(rgb, boxes)

	for encoding in encodings:

		knownEncodings.append(encoding)
		knownNames.append(name)
print("encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open('/media/nk/Work/smartglass_cloud/facedeeplearning/1.pickle', "wb")
f.write(pickle.dumps(data))
f.close()
