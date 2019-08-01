import numpy as np
import argparse
import array 
import cv2 as cv
inWidth = 300
inHeight = 300
WHRatio = inWidth / float(inHeight)
inScaleFactor = 0.007843
meanVal = 127.5
num_classes=90
thr=0.2
weights='odes/frozen_inference_graph.pb'
prototxt='odes/ssd_mobilenet_v1_coco.pbtxt'
assert(num_classes == 90)
net = cv.dnn.readNetFromTensorflow(weights, prototxt)
swapRB = True
classNames = { 0: 'background',
    1: 'người', 2: 'xe đạp', 3: 'xe hơi', 4: 'xe máy', 5: 'máy bay', 6: 'xe buýt',
    7: 'xe lửa', 8: 'xe tải', 9: 'thuyền', 10: 'đèn giao thông', 11: 'vòi cứu hỏa',
    13: 'dấu hiệu dừng', 14: 'đồng hồ đỗ xe', 15: 'ghế', 16: 'chim', 17: 'mèo',
    18: 'chó', 19: 'ngựa', 20: 'cừu', 21: 'bò', 22: 'voi', 23: 'gấu',
    24: 'ngựa vằn', 25: 'hươu cao cổ', 27: 'ba lô', 28: 'ô', 31: 'túi xách',
    32: 'tie', 33: 'vali', 34: 'frisbee', 35: 'ván trượt', 36: 'ván trượt tuyết',
    37: 'Quả bóng thể thao', 38: 'diều', 39: 'gậy bóng chày', 40: 'găng tay bóng chày',
    41: 'ván trượt', 42: 'ván lướt sóng', 43: 'vợt tennis', 44: 'chai',
    46: 'ly rượu', 47: 'chén', 48: 'nĩa', 49: 'dao', 50: 'muỗng',
    51: 'bát', 52: 'chuối', 53: 'táo', 54: 'bánh sandwich', 55: 'cam',
    56: 'bông cải xanh', 57: 'cà rốt', 58: 'hot dog', 59: 'pizza', 60: 'donut',
    61: 'bánh', 62: 'ghế', 63: 'ghế', 64: 'chậu cây', 65: 'giường',
    67: 'bàn ăn', 70: 'nhà vệ sinh', 72: 'tv', 73: 'máy tính xách tay', 74: 'chuột',
    75: 'từ xa', 76: 'bàn phím', 77: 'điện thoại di động', 78: 'vi sóng', 79: 'lò',
    80: 'lò nướng', 81: 'chìm', 82: 'tủ lạnh', 84: 'sách', 85: 'đồng hồ',
    86: 'bình', 87: 'kéo', 88: 'gấu bông', 89: 'máy sấy tóc', 90: 'bàn chải đánh răng'}
def classfy():
    txt=""
    i=0
    check=[]
    for i in range(100):
       check.append(False)
    result=""
    able=[2,3,4,5,6,7,8,10,27,48,49,50,77,87]
    path="image.jpg"
    if (1==1):
        maxx=0
        frame=cv.imread(path)
        blob = cv.dnn.blobFromImage(frame, inScaleFactor, (inWidth, inHeight), (meanVal, meanVal, meanVal), swapRB)
        net.setInput(blob)
        detections = net.forward()

        cols = frame.shape[1]
        rows = frame.shape[0]

        if cols / float(rows) > WHRatio:
            cropSize = (int(rows * WHRatio), rows)
        else:
            cropSize = (cols, int(cols / WHRatio))

        y1 = int((rows - cropSize[1]) / 2)
        y2 = y1 + cropSize[1]
        x1 = int((cols - cropSize[0]) / 2)
        x2 = x1 + cropSize[0]
        frame = frame[y1:y2, x1:x2]

        cols = frame.shape[1]
        rows = frame.shape[0]

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > thr:
                class_id = int(detections[0, 0, i, 1])

                xLeftBottom = int(detections[0, 0, i, 3] * cols)
                yLeftBottom = int(detections[0, 0, i, 4] * rows)
                xRightTop   = int(detections[0, 0, i, 5] * cols)
                yRightTop   = int(detections[0, 0, i, 6] * rows)

                cv.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
                              (0, 255, 0))
                if class_id in classNames:
                    label = classNames[class_id] + ": " + str(confidence)
                    print(label)
                    if (check[class_id]==False) and (class_id != 1):
                        check[class_id]=True
                        txt = txt+classNames[class_id]+','
        return txt