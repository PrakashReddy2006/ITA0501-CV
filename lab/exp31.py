# Experiment 31: Image Segmentation using Thresholding
import cv2

img = cv2.imread("flower.jpeg")
if img is None:
    raise SystemExit("Put flower.jpeg in this folder.")
img = cv2.resize(img, (500, 350))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, segmented = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", img)
cv2.imshow("Segmented Image", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
