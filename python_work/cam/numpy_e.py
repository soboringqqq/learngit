import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('real_world.png')

# access a pixel
px = img[100,100]
print(px)

# accessing only blue pixel
blue = img[100,100,0]
print(blue)

# properties image
print(img.shape)

# total number if pixels
print(img.size)

# image datatypr
print(img.dtype)

BLUE = [255,0,0]
constant= cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.imshow(constant,'gray')
plt.show()

