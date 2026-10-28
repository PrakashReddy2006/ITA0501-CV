import cv2

img = cv2.imread("flower.jpeg")

if img is None:
    print("Image not found!")
    exit()

h, w = img.shape[:2]

# Select a region
x, y = w//4, h//4
roi = img[y:y+h//4, x:x+w//4].copy()

# Copy the image
result = img.copy()

# Paste the region into another location
rh, rw = roi.shape[:2]
result[0:rh, 0:rw] = roi

cv2.imshow("Original Image", img)
cv2.imshow("Cropped Region", roi)
cv2.imshow("Copy and Paste", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
