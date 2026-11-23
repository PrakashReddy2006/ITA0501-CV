import cv2

img = cv2.imread("flower.jpeg")
img = cv2.resize(img, (500, 350))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)

cv2.imshow("Original Image", gray)
cv2.imshow("Histogram Equalization", equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
