import cv2

img = cv2.imread("flower.jpeg")
img = cv2.resize(img, (500, 350))
h, w = img.shape[:2]

x, y = w // 4, h // 4
roi = img[y:y+h//4, x:x+w//4].copy()

result = img.copy()
rh, rw = roi.shape[:2]
result[0:rh, 0:rw] = roi

cv2.imshow("Original Image", img)
cv2.imshow("Cropped Region", roi)
cv2.imshow("Copy and Paste", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
