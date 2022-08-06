import cv2 as cv
import numpy as np

#img = cv.imread("./Resources/Photos/cat.jpg")
##Draw over an image
#
#
#
#cv.imshow("Cat", img)



#Making a blank image using numpy.zeros function

blank = np.zeros((500, 500, 3), dtype="uint8")
#cv.imshow("Blank", blank)


#Paint over a blank image(Making a big red dot)

#blank[200:300, 200:300]=0, 0, 25
#red_dot = blank
#print(red_dot)
#cv.imshow("Big red dot", red_dot)

#Draw a rectangle using opencv method rectangle(img, pt1, pt2, (B, G, R), thickness)

cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=10) 
#thickness=cv.FILLED or -1, will give you a filled reactangle

#Drawing a cercle using opencv method cercle(img, center, rad, (b,g,r), thickness)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 20, (0, 0, 255), thickness = -1)


cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(255, 0, 0), thickness = 10)

#Write a text over an image

cv.putText(blank, "Hello Opencv", (250, 450), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Hello", blank)

cv.waitKey(0)



















