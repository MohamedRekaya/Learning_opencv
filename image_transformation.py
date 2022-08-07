import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/lady.jpg")
cv.imshow("girl", img)

#Transformation
#def translate(img, x, y):
#    transMat = np.float32([[1, 0, x], [0, 1, y]])
#    dimensions = (img.shape[1], img.shape[0])
#    return cv.warpAffine(img, transMat, dimensions)
#
#translated = translate(img, -100, -100)
##cv.imshow("Lady", translated)
#
#
#def translate2(img, x, y):
#    blank = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype="uint8")
#    blank[x:, y:] = img[-x:, -y:]
#    return blank
#translated2 = translate(img, -100, -100)
##cv.imshow("Lady2", translated2)
#
height = img.shape[0]
width  = img.shape[1]
#print(height, width)
#for i in range(height):
#    for j in range(width):
#        rot_matrix =np.array([[ -1, 0], [0, -1]]) 
#        idx =np.array([[i-height//2,  j-img.shape[1]//2]]) 
#        rot_idx = np.dot(rot_matrix, np.transpose(idx))
#        blank[i, j] = img[rot_idx[0]+height//2 , rot_idx[1]+width//2]
#cv.imshow("fliped", blank)        
#
def rotation(img, deg, center, direction="COUNTERCLOCKWISE"):
    rad = deg*2*np.pi/360
    blank = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype="uint8")
    rot_mat = np.array([[np.cos(rad), np.sin(rad)], [-np.sin(rad), np.cos(rad)]])
    
    if (direction=="CLOCKWISE"):
        rot_mat = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
        
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            idx = np.array([[i-center[0]//2, j-center[1]//2]])
            rot_idx = np.dot(rot_mat, np.transpose(idx)).astype(int)
            if(rot_idx[0]+center[0]//2>=685 or rot_idx[1]+center[1]//2>=637 or rot_idx[0]+center[0]//2<0 or rot_idx[1]+center[1]//2<0):
                blank[i,j]=0, 0, 0
                continue
            blank[i, j] = img[rot_idx[0]+center[0]//2, rot_idx[1]+center[1]//2]
    print(rot_mat)
    return blank

rotated = rotation(img,45, (height, width), direction="CLOCKWISE" )

cv.imshow("flipped", rotated)





    





























cv.waitKey(0)
