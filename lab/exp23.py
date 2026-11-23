# Experiment 23: Top Hat
import cv2
import numpy as np

img = cv2.imread("flower.jpeg")
if img is None:
    raise SystemExit("Put flower.jpeg in this folder.")
img = cv2.resize(img, (500, 350))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((15, 15), np.uint8)
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original Gray Image", gray)
cv2.imshow("Top Hat", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
