# Experiment 26: Reverse Video Frames
# Required file: sample-1mb.mp4
import cv2

cap = cv2.VideoCapture("sample-1mb.mp4")
if not cap.isOpened():
    raise SystemExit("Put sample-1mb.mp4 in this folder.")

frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(cv2.resize(frame, (500, 350)))
cap.release()

for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
