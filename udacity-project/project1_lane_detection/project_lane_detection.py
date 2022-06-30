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

def laneDetection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gf_kernel = 5
    gf_gray = cv2.GaussianBlur(gray, (gf_kernel, gf_kernel), 0)
    minVal = 100
    maxVal = 150
    edges = cv2.Canny(gf_gray, minVal, maxVal)
    edges_ROI = ROI(edges)
    hough_lines = get_hough_lines(edges_ROI)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype = np.uint8)
    if hough_lines is not None:
            for line in hough_lines:
                x1, y1, x2, y2 = line.reshape(4) # converting to 1d array
                cv2.line(img, (x1, y1,), (x2, y2), color = (255, 0, 0), thickness = 2)
    res_img = cv2.addWeighted(img, 0.8, line_img, 1, 0)
    return res_img

# detect lanes on the video
def videolanes():
    videocap = cv2.VideoCapture('./data/test_videos/solidWhiteRight.mp4')
    while(videocap.isOpened()):
        ret, frame = videocap.read()
        frame = laneDetection(frame)
        cv2.imshow('lane detection', frame)
        # 1.waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).
        # 2.waitKey(1) will display a frame for 1 ms, after which display will be automatically closed.
        # Since the OS has a minimum time between switching threads,
        # the function will not wait exactly 1 ms, it will wait at least 1 ms,
        # depending on what else is running on your computer at that time.
        if cv2.waitKey(1) & 0xFF == ord('q'): # wait for 1ms until the user presses the 'q' key to quit the while loop
            break
    videocap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    videolanes()

