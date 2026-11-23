# Experiment 22: Morphological Closing
import cv2
import numpy as np

img = cv2.imread("flower.jpeg")
if img is None:
    raise SystemExit("Put flower.jpeg in this folder.")
img = cv2.resize(img, (500, 350))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Binary Image", binary)
cv2.imshow("Closing Image", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
