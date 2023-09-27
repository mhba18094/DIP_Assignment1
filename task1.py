import cv2 as cv
import numpy as np

image_org = cv.imread('coin.png',1)
resized_image = cv.resize(image_org,(256,256),interpolation=cv.INTER_AREA)
cv.imshow('Original Image',resized_image)
cv.waitKey(0)
