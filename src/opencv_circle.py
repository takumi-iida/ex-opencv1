import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

img = cv2.imread('grape.jpg',0)
gray_blurred = cv2.blur(img, (9,9 ))

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred,
                cv2.HOUGH_GRADIENT, 1, 40, param1 = 20, param2 = 25, minRadius = 55, maxRadius = 90)
print(detected_circles)

# Draw circles that are detected.
if detected_circles is not None:

    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
    cv2.imwrite("detect_circle.png", img)
