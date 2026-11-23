import cv2

# Read image
img = cv2.imread("face.jpg")

if img is None:
    print("Error: face.jpg not found!")
    raise SystemExit

# Resize image for consistent processing
img = cv2.resize(img, (600, 450))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load OpenCV's pre-trained Haar Cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Detect faces first to narrow down the search area and reduce false positives
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

total_eyes = 0

for (x, y, w, h) in faces:
    # Region of interest (ROI) for face in grayscale and color
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    # Detect eyes inside the face region
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))
    
    for (ex, ey, ew, eh) in eyes:
        # Draw rectangles around the eyes on the original image
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        total_eyes += 1

print("Eyes detected:", total_eyes)

# Display output
cv2.imshow("Eye Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
