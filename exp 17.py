import cv2

img = cv2.imread("flower.jpeg")

if img is None:
    print("Image not found!")
    exit()

result = img.copy()

cv2.putText(result, "MY WATERMARK", (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 0, 255), 2)

cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
