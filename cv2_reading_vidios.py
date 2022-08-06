import cv2 as cv


capture = cv.VideoCapture("./Resources/Videos/dog.mp4")


while(True):

    ret, frame = capture.read()
    cv.imshow("Dog Video", frame)

    if(cv.waitKey(20)  &  0xFF==ord("d")):
        break
capture.release()
cv.destroyallWindows()

