import cv2

img = cv2.imread("flower.jpeg")
small = cv2.resize(img, (300, 200))
large = cv2.resize(img, (500, 350))

cv2.imshow("Small Image", small)
cv2.imshow("Large Image", large)
cv2.waitKey(0)
cv2.destroyAllWindows()
