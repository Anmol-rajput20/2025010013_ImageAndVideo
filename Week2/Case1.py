import cv2
import numpy as np

# Read grayscale image
img = cv2.imread("grayscale.jpg", cv2.IMREAD_GRAYSCALE)

# Calculate mean intensity
threshold = np.mean(img)

# Convert to binary image
binary = np.where(img >= threshold, 255, 0).astype(np.uint8)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)

print("Mean Threshold =", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()