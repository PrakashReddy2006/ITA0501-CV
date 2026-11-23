# Experiment 38: Count Faces in an Image
# Required file: faces.jpg
import cv2

img = cv2.imread("faces.jpg")
if img is None:
    raise SystemExit("Put faces.jpg in this folder.")

img = cv2.resize(img, (600, 450))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(path)

faces = cascade.detectMultiScale(gray, 1.1, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

print("Total number of faces:", len(faces))
cv2.imshow("Face Count", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
