import cv2 as cv
import numpy as np

image_org = cv.imread('coin.png',1)
gray_image = cv.cvtColor(image_org,cv.COLOR_BGR2GRAY)

cv.imshow('Gray Image',gray_image)
cv.waitKey(0)
