import cv2
import numpy as np

# Read grayscale image
img = cv2.imread("grayscale.jpg", cv2.IMREAD_GRAYSCALE)

img = cv2.imread("grayscale.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

# Input threshold from user
threshold = int(input("Enter threshold value (0-255): "))

# Convert to binary image
binary = np.where(img >= threshold, 255, 0).astype(np.uint8)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()