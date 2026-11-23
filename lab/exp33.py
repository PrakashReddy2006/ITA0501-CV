# Experiment 33: Create a White Image with a Rectangle
import cv2
import numpy as np

img = np.full((400, 600, 3), 255, dtype=np.uint8)
cv2.rectangle(img, (150, 100), (450, 300), (0, 0, 255), 3)

cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
