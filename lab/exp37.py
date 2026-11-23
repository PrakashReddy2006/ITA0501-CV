# Experiment 37: Foreground Extraction using HSV Colour Levels
# Demo isolates a red object. Adjust HSV limits for the colour you want.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit("Could not open webcam.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (600, 400))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 100, 80])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 80])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    foreground = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Original Video", frame)
    cv2.imshow("Foreground", foreground)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
