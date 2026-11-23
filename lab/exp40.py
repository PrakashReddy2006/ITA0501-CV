import cv2
import pytesseract
import os

# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Check Tesseract
if not os.path.exists(pytesseract.pytesseract.tesseract_cmd):
    print("Tesseract not installed!")
    raise SystemExit

# Open video
cap = cv2.VideoCapture("text-video.mp4")

if not cap.isOpened():
    print("Video not found!")
    raise SystemExit

print("Extracting text from video...")

frame_number = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if frame_number % 15 == 0:

        gray = cv2.cvtColor(
            frame, cv2.COLOR_BGR2GRAY
        )

        text = pytesseract.image_to_string(gray).strip()

        if text:
            print("Frame:", frame_number)
            print("Extracted Text:", text)
            print("------------------")

        cv2.imshow("Text Extraction", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    frame_number += 1

cap.release()
cv2.destroyAllWindows()

print("Text extraction completed!")
