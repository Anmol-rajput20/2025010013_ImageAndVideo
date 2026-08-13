import cv2
import numpy as np

# Read image (OpenCV reads in BGR format)
img = cv2.imread("color.jpg")

# Split channels
B, G, R = cv2.split(img)

# Mean average
gray = ((R.astype(float) + G.astype(float) + B.astype(float)) / 3).astype(np.uint8)

# Display
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()