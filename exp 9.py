import cv2

img = cv2.imread("flower.jpeg")

big = cv2.resize(img, None, fx=1, fy=1)
small = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.imshow("Original Image", img)
cv2.imshow("Big Image", big)
cv2.imshow("Small Image", small)

cv2.waitKey(0)
cv2.destroyAllWindows()
