import cv2

cap = cv2.VideoCapture("sample-1mb.mp4")

if not cap.isOpened():
    print("Video not found!")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 30

mode = "normal"

while True:

    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    frame = cv2.resize(frame, (500, 350))
    cv2.imshow("Video Playback", frame)

    if mode == "fast":
        delay = 1
    elif mode == "slow":
        delay = 200
    else:
        delay = int(1000 / fps)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('f'):
        mode = "fast"

    elif key == ord('s'):
        mode = "slow"

    elif key == ord('n'):
        mode = "normal"

    elif key == ord('q'):
        break

    if mode == "fast":
        current = cap.get(cv2.CAP_PROP_POS_FRAMES)
        cap.set(cv2.CAP_PROP_POS_FRAMES, current + 19)

cap.release()
cv2.destroyAllWindows()
