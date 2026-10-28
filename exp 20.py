import cv2
import numpy as np

img = cv2.imread("flower.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(binary, kernel, iterations=1)

cv2.imshow("Original Image", binary)
cv2.imshow("Dilation Image", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
