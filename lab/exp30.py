import cv2

img = cv2.resize(cv2.imread("faces.jpg"), (600, 450))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=15, minSize=(25, 25))

for (x, y, w, h) in smiles:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print("Smile regions detected:", len(smiles))
cv2.imshow("Smile Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
