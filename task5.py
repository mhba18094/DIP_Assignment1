import cv2 as cv
import numpy as np

image_org = cv.imread('coin.png',1)
gray_image = cv.cvtColor(image_org,cv.COLOR_BGR2GRAY)

th,dst = cv.threshold(gray_image,160,255,cv.THRESH_BINARY)

params = cv.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100
params.maxArea = 100000

params.filterByColor = True
params.blobColor = 0

detector = cv.SimpleBlobDetector_create(params)
keypoints = detector.detect(dst)

blank = np.zeros((1,1))
blobs = cv.drawKeypoints(dst,keypoints,blank,(0,0,255),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number = len(keypoints)
blobs = cv.putText(blobs,"Total number of coins are: "+str(number),(100,100),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv.imshow('Keypoints',blobs)
cv.waitKey(0)
