import cv2
import numpy as np
import matplotlib.pyplot as plt



# Q1 - LOG TRANSFORMATION



img = cv2.imread("grayscale3.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

# c = 1
# Formula: s = c * log(1 + r)

log_image = np.log1p(img.astype(np.float32))


log_image = log_image / log_image.max() * 255


log_image = log_image.astype(np.uint8)



plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(log_image, cmap="gray")
plt.title("Log Transformed Image")
plt.axis("off")

plt.tight_layout()
plt.show()



# Q2 - POWER LAW / GAMMA TRANSFORMATION



gamma = float(input("Enter gamma value: "))


normalized = img / 255.0

# Power-law transformation
# Formula: s = c * r^gamma
# c = 1

gamma_image = np.power(normalized, gamma)


gamma_image = (gamma_image * 255).astype(np.uint8)



plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gamma_image, cmap="gray")
plt.title("Gamma Transformed Image")
plt.axis("off")

plt.tight_layout()
plt.show()


# Q3 - INTENSITY LEVEL SLICING / CONTRAST STRETCHING

input_low = int(input("Enter input lower intensity value: "))
input_high = int(input("Enter input upper intensity value: "))

# Desired output intensity range
output_low = int(input("Enter output lower intensity value: "))
output_high = int(input("Enter output upper intensity value: "))



if not (0 <= input_low < input_high <= 255):
    print("Invalid input intensity range!")
    exit()

if not (0 <= output_low <= output_high <= 255):
    print("Invalid output intensity range!")
    exit()


contrast_image = img.astype(np.float32)


contrast_image = (
    (contrast_image - input_low)
    * (output_high - output_low)
    / (input_high - input_low)
    + output_low
)


contrast_image = np.clip(contrast_image, 0, 255)


contrast_image = contrast_image.astype(np.uint8)



plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(contrast_image, cmap="gray")
plt.title("Contrast Stretched Image")
plt.axis("off")

plt.tight_layout()
plt.show()