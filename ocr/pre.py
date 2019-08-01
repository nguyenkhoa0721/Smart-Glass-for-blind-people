import cv2
import numpy as np
def his(img):
	img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
	img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
	img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
	return img
def contrast(img):
	clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
	lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) 
	l, a, b = cv2.split(lab)  
	l2 = clahe.apply(l)  
	lab = cv2.merge((l2,a,b))  
	img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
	return img
def PRE(img):
	img=his(img)
	img=contrast(img)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	return img