import cv2

img = cv2.imread("flower.jpeg")
img = cv2.resize(img, (500, 350))
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated = cv2.resize(rotated, (350, 500))

cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
