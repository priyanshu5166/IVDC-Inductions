# lane_detection_opencv
This project demonstrates lane detection in images using OpenCV. The algorithm processes an image, applies color filtering, defines a region of interest, and then detects lane lines using edge detection and the Hough Line Transform.

**Requirements**
To run the code, you need the following dependencies installed:

Python 3.x

OpenCV (Install using pip install opencv-python)

NumPy (Install using pip install numpy)

**How the Code Works**

Load the Image: The image is loaded from the specified path using cv.imread().

Convert to HSV Color Space: The loaded image is converted to the HSV color space to better handle color filtering.

Define Color Ranges for Yellow and White: These colors are used to detect road lanes. Yellow lanes and white lanes are identified using their respective HSV ranges.

**Create Masks:**

A mask is created for both yellow and white lanes using cv.inRange().

The two masks are combined using cv.bitwise_or().

Apply the Mask: The combined mask is applied to the original image using cv.bitwise_and().

**Region of Interest (ROI):**

A polygonal region is defined to limit the detection to the road area, where lane lines are expected.

The mask for the region is created using cv.fillPoly().


**Edge Detection:**

The image is converted to grayscale, and edges are detected using the Canny Edge Detector (cv.Canny()).

**Hough Line Transform:**

The Hough Line Transform (cv.HoughLinesP()) is used to detect lines in the edge-detected image.

Detected lines are drawn on the original image.

**Inverted Mask:**

The detected lane lines are further processed by inverting the image to highlight lanes.

Displaying Results: The final image with detected lane lines is displayed using cv.imshow().

**Output**

Detected Lanes: The script will show an image with the detected lane lines highlighted.

Masked ROI Lines: A binary image of the detected lanes is also displayed.

**Results**

original image:

![test3](https://github.com/user-attachments/assets/2e919563-7a92-4560-a210-51b775997683)

image with lanes:

![image](https://github.com/user-attachments/assets/2e835f6b-9fa9-4641-84dc-6a7f9e9a0ed6)

bitmap without surrounding:

![Screenshot 2024-09-08 231337](https://github.com/user-attachments/assets/3f11d32d-ee6a-4ca6-bae3-4e1c35842fd3)




