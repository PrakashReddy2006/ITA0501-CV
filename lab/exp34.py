# Experiment 34: Create a White Image with a Circle
import cv2
import numpy as np

img = np.full((400, 600, 3), 255, dtype=np.uint8)
cv2.circle(img, (300, 200), 100, (0, 255, 0), 3)

cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
