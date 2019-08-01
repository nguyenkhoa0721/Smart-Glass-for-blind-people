from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
model = load_model("fashion/fashion.model")
mlb=['đen','xanh','váy','quần jeans','đỏ','áo sơ mi']
def FASHION():
	image = cv2.imread("image.jpg")
	output = imutils.resize(image, width=400)
	image = cv2.resize(image, (96, 96))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	proba = model.predict(image)[0]
	idxs = np.argsort(proba)[::-1][:2]
	result=[]
	for (i, j) in enumerate(idxs):
		label = "{}".format(mlb[j])
		result.append(label)
	string= result[1]+" "+result[0]
	for (label, p) in zip(mlb, proba):
		print("{}: {:.2f}%".format(label, p * 100))
	return string

