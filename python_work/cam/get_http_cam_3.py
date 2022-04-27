import cv2 as cv
import numpy as np

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

esp_ip = "192.168.0.103"
vcap = cv.VideoCapture(f"rtsp://{esp_ip}/mjpeg/1")
# save the video


while True:
    ret, frame = vcap.read()

    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    # for (x, y, w, h) in faces:
        # frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv.imshow("Frame", frame)
    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vcap.release()
cv.destroyAllWindows()
