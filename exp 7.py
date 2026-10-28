import cv2

cap = cv2.VideoCapture("sample-1mb.mp4")

delay = 100

while True:
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow("Video", frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        delay = 300
    elif key == ord('f'):
        delay = 1
    elif key == ord('n'):
        delay = 30

cap.release()
cv2.destroyAllWindows()
