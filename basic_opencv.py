import cv2 as cv


img = cv.imread("./Resources/Photos/cat.jpg")

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Bluring an image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#cv.imshow("Cat Blured", blur)
#To increase the blur simply increasing the window size
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow("Cat even more blured", blur)

#Implementing Canny edge detector
cat_edges = cv.Canny(img, 175, 200)
#cv.imshow("Cat Edges", cat_edges)

#Reducing the edges by applying canny edge detecor with a blured image
cat_edges = cv.Canny(blur, 150, 175)
cv.imshow("cat Edges", cat_edges)

#Dialating the iamge edges by passing canny edge detecting for example

dialated = cv.dilate(cat_edges, (5, 5), iterations=5)
cv.imshow("Dialated Edges", dialated)

#Oroded Edges

eroded = cv.erode(dialated, (5, 5), iterations=5)
cv.imshow("Eroded Edges", eroded)

#Resizing an image by usnig INTER_AREA, INTER_LINEAR, INTER_CUBIC
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
cv.imshow("resized Cat", resized )

#Cropping an image
cropped = img[50:200, 200:400]
cv.imshow("cropped image", cropped )

cv.waitKey(0)

