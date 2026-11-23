# Experiment 27: Face Detection in an Image
# Required file: face.jpg
import cv2

img = cv2.imread("face.jpg")
if img is None:
    raise SystemExit("Put face.jpg in this folder.")

img = cv2.resize(img, (600, 450))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

faces = face_cascade.detectMultiScale(gray, 1.1, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

print("Faces detected:", len(faces))
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
