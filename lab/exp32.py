# Experiment 32: White Image with Four Coloured Corner Boxes
import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

if width <= 0 or height <= 0:
    raise SystemExit("Width and height must be positive.")

img = np.full((height, width, 3), 255, dtype=np.uint8)
box_w = max(1, width // 10)
box_h = max(1, height // 10)

cv2.rectangle(img, (0, 0), (box_w-1, box_h-1), (0, 0, 0), -1)  # black
cv2.rectangle(img, (width-box_w, 0), (width-1, box_h-1), (255, 0, 0), -1)  # blue
cv2.rectangle(img, (0, height-box_h), (box_w-1, height-1), (0, 255, 0), -1)  # green
cv2.rectangle(img, (width-box_w, height-box_h), (width-1, height-1), (0, 0, 255), -1)  # red

preview = cv2.resize(img, (600, 400))
cv2.imshow("Four Corner Boxes", preview)
cv2.waitKey(0)
cv2.destroyAllWindows()
