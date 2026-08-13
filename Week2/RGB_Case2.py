import cv2
import numpy as np

# Read image
img = cv2.imread("color.jpg")

# Split channels
B, G, R = cv2.split(img)

# Input weights
wr = float(input("Enter weight for Red (0-1): "))
wg = float(input("Enter weight for Green (0-1): "))
wb = float(input("Enter weight for Blue (0-1): "))

# Check validity
if wr < 0 or wg < 0 or wb < 0 or wr > 1 or wg > 1 or wb > 1:
    print("Each weight must be between 0 and 1.")

elif abs((wr + wg + wb) - 1.0) > 1e-6:
    print("Sum of weights must be equal to 1.")

else:
    gray = (wr * R + wg * G + wb * B).astype(np.uint8)

    cv2.imshow("Original", img)
    cv2.imshow("Grayscale", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()