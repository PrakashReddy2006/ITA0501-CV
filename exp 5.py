import cv2
import matplotlib.pyplot as plt

img = cv2.imread("flower.jpeg")

colors = ("b", "g", "r")

for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)

plt.title("Color Histogram")
plt.xlabel("Color Level")
plt.ylabel("Number of Pixels")
plt.show()
