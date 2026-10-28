import cv2
import numpy as np

img = cv2.imread("flower.jpeg")

if img is None:
    print("Image not found!")
    exit()

h, w = img.shape[:2]

p1 = np.float32([[0, 0], [w-1, 0],
                 [0, h-1], [w-1, h-1]])

p2 = np.float32([[50, 50], [w-51, 0],
                 [0, h-1], [w-1, h-51]])

M = cv2.getPerspectiveTransform(p1, p2)
result = cv2.warpPerspective(img, M, (w, h))

cv2.imshow("Original", img)
cv2.imshow("Perspective Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
