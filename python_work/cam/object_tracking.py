import numpy as np
import cv2 as cv

# cap = cv.VideoCapture('output.avi')

# while(1):
	# # Take each frame
    # _, frame = cap.read()
    # # Convert BGR to HSV
    # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # # define range of blue color in HSV
    # lower_red = np.array([51,51,0])
    # upper_red = np.array([0,102,0])
    # # Threshold the HSV image to get only blue colors
    # mask = cv.inRange(hsv, lower_red, upper_red)
    # # Bitwise-AND mask and original image
    # res = cv.bitwise_and(frame,frame, mask= mask)
    # cv.imshow('frame',frame)
    # cv.imshow('mask',mask)
    # cv.imshow('res',res)
    # k = cv.waitKey(5) & 0xFF
    # if k == 27:
        # break
# cv.destroyAllWindows()


# cap = cv.imread('blue_cap.jpg')


# hsv = cv.cvtColor(cap, cv.COLOR_BGR2HSV)
# # define range of blue color in HSV
# lower_red = np.array([46,39,37])
# upper_red = np.array([159,235,220]) # upper must greater than lower
# # Threshold the HSV image to get only blue colors
# mask = cv.inRange(hsv, lower_red, upper_red)
# # Bitwise-AND mask and original image
# res = cv.bitwise_and(cap,cap, mask= mask)
# cv.imshow('frame',cap)
# cv.imshow('mask',mask)
# cv.imshow('res',res)
# cv.waitKey(0)    
# cv.destroyAllWindows()


# use BGR color

# cap = cv.imread('blue_cap.jpg')


# hsv = cv.cvtColor(cap, cv.COLOR_BGR2HSV)
# # define range of blue color in HSV
# lower_red = np.uint8([0,0,128])
# upper_red = np.uint8([150,255,255]) # upper must greater than lower 
# # Threshold the HSV image to get only blue colors
# mask = cv.inRange(cap, lower_red, upper_red) # not use hsv
# # Bitwise-AND mask and original image
# res = cv.bitwise_and(cap,cap, mask= mask)
# cv.imshow('frame',cap)
# cv.imshow('mask',mask)
# cv.imshow('res',res)
# cv.imshow('hsv',hsv)
# cv.waitKey(0)    
# cv.destroyAllWindows()


cap = cv.imread('blue_cap.jpg')


hsv = cv.cvtColor(cap, cv.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_red = np.array([78,43,46])
upper_red = np.array([99,255,255]) # upper must greater than lower 
# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_red, upper_red) # not use hsv
# Bitwise-AND mask and original image
res = cv.bitwise_and(cap,cap, mask= mask)
cv.imshow('frame',cap)
cv.imshow('mask',mask)
cv.imshow('res',res)
cv.imshow('hsv',hsv)
cv.waitKey(0)    
cv.destroyAllWindows()


