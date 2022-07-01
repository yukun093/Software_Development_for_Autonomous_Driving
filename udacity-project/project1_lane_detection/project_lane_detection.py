import matplotlib.image as mplimg
from matplotlib import pyplot as plt
import cv2
import numpy as np

def ROI(edges):
    height = edges.shape[0]
    width = edges.shape[1]
    # define Triangular ROI: when the values will change according to the place of camera mounts
    triangle = np.array([[(100, height), (width, height), (width-500, int(height/1.9))]])
    # create full black area same as that of input image
    black_edges = np.zeros_like(edges)
    # put the triangular shape on top of our black image to create a mask
    mask = cv2.fillPoly(black_edges, triangle, 255)
    # apply mask on the original image
    masked_edges = cv2.bitwise_and(edges, mask)
    return masked_edges

def get_hough_lines(edges_ROI):
    hough_lines =  cv2.HoughLinesP(edges_ROI, rho = 1.0, theta = np.pi / 180, threshold = 60, minLineLength = 40, maxLineGap = 20)
    return hough_lines

def calculate_coordinates(img, parameters):
    slope, b_intercept = parameters
    # Sets initial y1 as height from top down (bottom of the frame)
    y1 = img.shape[0]
    # Sets final y2 as 225(the larger the value is, the longer the line is) above the bottom of the frame
    y2 = int(y1 * (3.4 / 5))
    # Sets initial x2 as (y1 - b) / m since y1 = mx1 + b
    x1 = int((y1 - b_intercept) / slope)
    # Sets initial x2 as (y2 - b) / m since y2 = mx2 + b
    x2 = int((y2 - b_intercept) / slope)
    return np.array([x1, y1, x2, y2])

def calculateLines(img ,hough_lines):
    left = []
    right = []
    # iterate all lines that are detected
    for line in hough_lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        b_intercept = parameters[1]
        if(slope < 0):
            left.append((slope, b_intercept))
        else:
            right.append((slope, b_intercept))
    # average out all the values for left and right into a single slope and b_intercept value for each line in the list
    left_avg = np.average(left, axis = 0)
    right_avg = np.average(right, axis = 0)
    # calculate x1, x2, y1, y2 coordinates for one line
    left_line = calculate_coordinates(img, left_avg)
    right_line = calculate_coordinates(img, right_avg)
    return np.array([left_line, right_line])

def displaylane(img, lines):
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype = np.uint8)
    if lines is not None:
            for x1, y1, x2, y2 in lines:
                cv2.line(img, (x1, y1,), (x2, y2), color = (0, 255, 0), thickness = 3) # color = (blue, green, red) for sequence
    line_img = cv2.addWeighted(img, 0.8, line_img, 1, 1)
    return line_img

def laneDetection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gf_kernel = 5
    gf_gray = cv2.GaussianBlur(gray, (gf_kernel, gf_kernel), 0)
    minVal = 100
    maxVal = 150
    edges = cv2.Canny(gf_gray, minVal, maxVal)
    edges_ROI = ROI(edges)
    hough_lines = get_hough_lines(edges_ROI)
    lines = calculateLines(img ,hough_lines)
    line_img = displaylane(img, lines)
    cv2.imshow('result', line_img)
    return line_img

# detect lanes on the image
def imagelanes():
    imagecap = cv2.imread('./data/test_images/solidWhiteCurve.jpg')
    detectedlines = laneDetection(imagecap)
    plt.imshow(detectedlines)
    plt.show()

# detect lanes on the video
def videolanes():
    cap = cv2.VideoCapture('./data/test_videos/solidWhiteRight.mp4')
    while(cap.isOpened()):
        ret, frame = cap.read()
        detectedLines = laneDetection(frame)
        # cv2.imshow('lane detection', detectedLines)
        # 1.waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).
        # 2.waitKey(1) will display a frame for 1 ms, after which display will be automatically closed.
        # Since the OS has a minimum time between switching threads,
        # the function will not wait exactly 1 ms, it will wait at least 1 ms,
        # depending on what else is running on your computer at that time.
        if cv2.waitKey(250) & 0xFF == ord('q'): # wait for 1ms until the user presses the 'q' key to quit the while loop
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # imagelanes()
    videolanes()

