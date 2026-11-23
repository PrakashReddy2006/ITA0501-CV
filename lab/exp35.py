# Experiment 35: Add User-Entered Text to an Image
import cv2

img = cv2.imread("flower.jpeg")
if img is None:
    raise SystemExit("Put flower.jpeg in this folder.")
img = cv2.resize(img, (500, 350))

message = input("Enter text: ")
cv2.putText(img, message[:35], (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

cv2.imshow("Image with Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
