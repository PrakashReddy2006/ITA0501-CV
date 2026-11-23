import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera not found!")
    exit()

print("Camera started successfully!")
print("Press Q to exit")

while True:

    ret, frame = cap.read()

    if not ret or frame is None:
        print("Cannot capture video")
        break

    # Resize frame
    frame = cv2.resize(frame, (640, 480))

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Green colour range
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Remove noise
    mask = cv2.medianBlur(mask, 5)

    # Extract green background
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display windows
    cv2.imshow("Original Webcam", frame)
    cv2.imshow("Detected Green Background", result)
    cv2.imshow("Background Mask", mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
