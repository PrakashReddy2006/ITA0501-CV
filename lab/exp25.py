# Experiment 25: Simple Watch Object Recognition using Template Matching
# Required files: watch.jpg (template) and scene.jpg (image containing the watch)
import cv2

template = cv2.imread("watch.jpg", 0)
scene = cv2.imread("scene.jpg", 0)

if template is None or scene is None:
    raise SystemExit("Put watch.jpg and scene.jpg in this folder.")

scene = cv2.resize(scene, (600, 450))
th, tw = template.shape[:2]

if th > scene.shape[0] or tw > scene.shape[1]:
    raise SystemExit("watch.jpg must be smaller than scene.jpg.")

result = cv2.matchTemplate(scene, template, cv2.TM_CCOEFF_NORMED)
_, score, _, location = cv2.minMaxLoc(result)

if score > 0.5:
    top_left = location
    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(scene, top_left, bottom_right, 255, 2)
    print("Possible watch found. Match score:", round(score, 2))
else:
    print("Watch not found. Match score:", round(score, 2))

cv2.imshow("Watch Recognition", scene)
cv2.waitKey(0)
cv2.destroyAllWindows()
