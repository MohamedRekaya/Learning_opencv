import cv2 as cv


#img = cv.imread("./Resources/Photos/cat.jpg")
#Reading a bigger image
img = cv.imread("./Resources/Photos/cat_large.jpg")

cv.imshow("Cat", img)

cv.waitKey(0)
