#It's all about contours, how to find them and draw them out using opencv funcitons such as cv.findContours() and cv.drawContours().
#What are contours:
    #Contours can be explained simply as a curve joining all the continous points(along the boundary), haivng same color or intensity.The contours are a useful tool for shape analysis and object detection and recognition.
    #-->For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
    #-->Since OpenCV 3.2, findContours() no longer modifies the source image but returns a modified image as the first of three return params.
    #-->In OpenCV finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

#Let's find contours of a binary image:
import numpy as np
import cv2 as cv

img = cv.imread("./Resources/Photos/cats.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 127, 255, 0)
cv.imshow("Thresholded Image", thresh)

img_thresh, contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#So how to draw the contours?
blank = np.zeros(img.shape, dtype="uint8")
cv.drawContours(blank, contours, -1, (0, 255, 0), 1)
cv.imshow("Contoured Image", blank)

cv.waitKey(0)
