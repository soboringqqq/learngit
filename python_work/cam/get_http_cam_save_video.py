import cv2 as cv
import numpy as np


esp_ip = "192.168.0.103"
vcap = cv.VideoCapture(f"rtsp://{esp_ip}/mjpeg/1")
# save the video
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (1600,  1200))

while True:
    ret, frame = vcap.read()
	
    #frame = cv.flip(frame, 0)
    out.write(frame)
	
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord('q'):
        break

vcap.release()
out.release()
cv.destroyAllWindows()
