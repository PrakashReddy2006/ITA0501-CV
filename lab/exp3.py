import cv2

img = cv2.imread("flower.jpeg")
img = cv2.resize(img, (500, 350))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original Image", img)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
