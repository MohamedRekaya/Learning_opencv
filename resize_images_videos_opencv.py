import cv2 as cv

#Resize Function

def rescaleFrame(frame, scale=0.5):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)    

#Change the resolution of a live video

def reschange(width, height):
    capture.set(3, width)
    capture.set(4, height)
"""
img = cv.imread("./Resources/Photos/cat_large.jpg")
print(img.shape)

img = rescaleFrame(img)
cv.imshow("Cat", img)

cv.waitKey(0)
"""
#Resizing a Video
capture = cv.VideoCapture("./Resources/Videos/dog.mp4")


while (True):

    ret, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2) 
    cv.imshow("A Dog Video", frame)
    cv.imshow("A Dog Video", frame_resized)
    if (cv.waitKey(20) & 0xff==ord('d')):
        break

capture.release()
cv.destroyAllWindows()







