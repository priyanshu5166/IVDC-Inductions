import cv2 as cv
import numpy as np

# main

img = cv.imread("C:/opencv/test3.jpg")

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Define color ranges for yellow and white
lower_yellow = np.array([18, 94, 140])
upper_yellow = np.array([48, 255, 255])
lower_white = np.array([0, 0, 160])
upper_white = np.array([180, 30, 255])

# Create masks for yellow and white
mask_yellow = cv.inRange(hsv, lower_yellow, upper_yellow)
mask_white = cv.inRange(hsv, lower_white, upper_white)

# Combine the masks
combined_mask = cv.bitwise_or(mask_yellow, mask_white)

# Apply the combined mask to the original image
masked_img = cv.bitwise_and(img, img, mask=combined_mask)

# region of interest (ROI)
height, width = img.shape[:2]
roi = np.array([[(200, height), (width - 50, height), (width // 2 + 5, height*0.579), (width // 2 +10, height*0.579)]], dtype=np.int32)

# Create a mask with the ROI
roi_mask = np.zeros_like(masked_img)
cv.fillPoly(roi_mask, roi, (255, 255, 255))
roi_mask = cv.cvtColor(roi_mask, cv.COLOR_BGR2GRAY)

masked_roi = cv.bitwise_and(masked_img, masked_img, mask=roi_mask)

gray_masked = cv.cvtColor(masked_roi, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray_masked, 100, 150)
edges1 = cv.Canny(gray_masked, 100, 150)

lines = cv.HoughLinesP(edges, 2, np.pi / 180, 50, minLineLength=50, maxLineGap=125)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv.line(edges1, (x1, y1), (x2, y2), (255, 0, 0), 3)

inverted = cv.bitwise_not(edges1)
masked_roi1 = cv.bitwise_and(inverted, inverted, mask=roi_mask)
masked_roi1=cv.bitwise_not(masked_roi1)

cv.imshow('result', masked_roi1)
cv.imshow("Detected Lanes", img)
cv.waitKey(0)
cv.destroyAllWindows()




