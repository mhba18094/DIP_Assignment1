import cv2 as cv
import numpy as np

image_org = cv.imread('coin.png',1)
gray_image = cv.cvtColor(image_org,cv.COLOR_BGR2GRAY)
th,dst = cv.threshold(gray_image,160,255,cv.THRESH_BINARY)

cv.imshow('Binary Image',dst)
cv.waitKey(0)

