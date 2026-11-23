# Experiment 28: Simple Moving Vehicle Detection in a Video
# Required file: vehicle.mp4
# This detects moving objects; it is a basic demonstration, not a vehicle classifier.
import cv2

cap = cv2.VideoCapture("vehicle.mp4")
if not cap.isOpened():
    raise SystemExit("Put vehicle.mp4 in this folder.")

subtractor = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (600, 400))
    mask = subtractor.apply(frame)
    mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 900:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Moving Vehicle Detection", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
