import cv2
import numpy as np
from object_detection import ObjectDetection


#Loading ObjectDetection
od = ObjectDetection()


cap = cv2.VideoCapture("D:\\KOVIDH KUMAR D S\\KOVIDH KUMAR D S PYTHON\\PYTHON 2022\\PYTHON PROJECTS\\OPEN CV PROJECTS\\OBJECT DETECTION FULL IN DEPTH\\Downloaded\\los_angeles.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #Detec objects on the frame
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes:
        (x, y, w, h) = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     print(box)
    # print("---------------------------------")

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()