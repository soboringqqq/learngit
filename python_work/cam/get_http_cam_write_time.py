import cv2 as cv
import numpy as np
import time

def write_text(img, text):
    # text = "FONT_HERSHEY_DUPLEX"
    position = (10, 1000)
    font = cv.FONT_HERSHEY_SIMPLEX
    size = 1
    color = (0, 255, 255)
    thickness = 2
    lineType =  cv.LINE_AA
    cv.putText(img, text, position, font, size, color, thickness, lineType)

    return img

Ts = time.time()
cnt = 0
before_time = 0

esp_ip = "192.168.0.103"
vcap = cv.VideoCapture(f"rtsp://{esp_ip}/mjpeg/1")
# save the video
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (1600,  1200))

while True:
    ret, frame = vcap.read()
    
    cnt = cnt + 1
    time_pass = time.time()-Ts
    localtime = time.asctime(time.localtime(time.time()))
    info_text = "Time: {:.2f}, Frame count: {:08d}, fps: {:.2f}, fps_one: {:.2f}, time: {}".format(time_pass, cnt, cnt/time_pass, 1/(time_pass-before_time), localtime)
    frame = write_text(frame, info_text)
	
    #frame = cv.flip(frame, 0)
    out.write(frame)
	
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord('q'):
        break

vcap.release()
out.release()
cv.destroyAllWindows()
