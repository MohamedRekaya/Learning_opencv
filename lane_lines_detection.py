import cv2 as cv
import numpy as np
import math

#Gray scale function
def grayscale(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Canny edge detection function
def canny(img, low_threshold, high_threshold):
    return cv.Canny(img, low_threshold, high_threshold)

#Bluring function
def guassian_blur(img, kernel_size):
    return cv.GaussianBlur(img, (kernel_size, kernel_size), 0)

#region of interest
def region_of_interest(img, vertices):
    #defining a blank mask to start with
    mask = np.zeros_like(img)
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape)>2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,)*channel_count
    else:
        ignore_mask_color = 255

    #Filling pixels inside the polygon defined by "vertices"with the fill color
    cv.fillPoly(mask, vertices, ignore_mask_color)

    #returning the image only where mask pixels are nonzero
    masked_image = cv.bitwise_and(img, mask)
    return masked_image



def draw_lines(img, lines, color=[255, 0, 0], thickness=7):

     #list to get positives and negatives values

    x_bottom_pos = []
    x_upperr_pos = []
    x_bottom_neg = []
    x_upperr_neg = []

    y_bottom = 700
    y_upperr = 450

    #y1 = slope*x1 + b
    #b = y1 - slope*x1
    #y = slope*x + b
    #x = (y - b)/slope

    slope = 0
    b = 0

    #get x upper and bottom to lines with slope positive and negative
    try:
        print(lines) 
        for line in lines:
            for x1,y1,x2,y2 in line:
                 #test and filter values to slope
                if ((y2-y1)/(x2-x1)) > 0.5 and ((y2-y1)/(x2-x1)) < 0.8 :

                    slope = ((y2-y1)/(x2-x1))
                    b = y1 - slope*x1

                    x_bottom_pos.append((y_bottom - b)/slope)
                    x_upperr_pos.append((y_upperr - b)/slope)

                elif ((y2-y1)/(x2-x1)) < -0.5 and ((y2-y1)/(x2-x1)) > -0.8:

                    slope = ((y2-y1)/(x2-x1))
                    b = y1 - slope*x1

                    x_bottom_neg.append((y_bottom - b)/slope)

                    x_upperr_neg.append((y_upperr - b)/slope)
    except:
        pass


    #creating a new 2d array with means
    try:
        lines_mean = np.array([[int(np.mean(x_bottom_pos)), int(np.mean(y_bottom)), int(np.mean(x_upperr_pos)), int(np.mean(y_upperr))],
                           [int(np.mean(x_bottom_neg)), int(np.mean(y_bottom)), int(np.mean(x_upperr_neg)), int(np.mean(y_upperr))]])
    

    #Drawing the lines
        for i in range(len(lines_mean)):
            cv.line(img, (lines_mean[i,0], lines_mean[i,1]), (lines_mean[i,2], lines_mean[i,3]), color, thickness)
    except:
        pass

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.

    Returns an image with hough lines drawn.
    """
    lines = cv.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img
def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.
    
    `initial_img` should be the image before any processing.
    
    The result image is computed as follows:
    
    initial_img * α + img * β + λ
    NOTE: initial_img and img must be the same shape!
    """
    return cv.addWeighted(initial_img, α, img, β, λ)

#Lane Finding Pipline



#Applying blur to avoid noise

#Finding Edges Using Canny


#Define Vertices to create a region of interest

vertices = np.array([[(200,650),(500, 400), (650, 400), (1000,650)]], dtype=np.int32)

#Use Hough Transformatioin to find lines
rho = 3
theta = np.pi/180
threshold = 15
min_line_len = 50
max_line_gap = 50




cap = cv.VideoCapture("./labeled/3.hevc")


while(True):


    ret, img = cap.read()

    gray = grayscale(img)
    kernel_size = 5 
    blur_gray = guassian_blur(gray, kernel_size)
    low_threshold = 50
    high_threshold = 150

    edges = canny(blur_gray, low_threshold, high_threshold)
    mask = region_of_interest(img, vertices)
    cv.imshow("masked", mask)
    masked_edges = region_of_interest(edges, vertices)
    cv.imshow("masked_edges", masked_edges)

    lines = hough_lines(masked_edges, rho, theta, threshold, min_line_len, max_line_gap)
    cv.imshow("lines", lines)
    
    lines_edges = weighted_img(lines, img, α=0.8, β=1., λ=0.)

   
    cv.imshow("la", lines_edges)
    if(cv.waitKey(50) & 0xff==ord("d")):
        break

cap.release()
cv.destroyAllWindows()






