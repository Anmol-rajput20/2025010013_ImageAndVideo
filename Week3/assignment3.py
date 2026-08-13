import cv2
import numpy as np
import matplotlib.pyplot as plt




gray_img = cv2.imread("grayscale2.jpg", cv2.IMREAD_GRAYSCALE)
bgr_img = cv2.imread("color2.jpg")

if gray_img is None:
    print("Error: grayscale2.jpg not found!")
    exit()

if bgr_img is None:
    print("Error: color2.jpg not found!")
    exit()

rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)



threshold = 127

_, binary_img = cv2.threshold(
    gray_img,
    threshold,
    255,
    cv2.THRESH_BINARY
)




print("\n--- BORDER / PADDING ---")

border_width = int(
    input("Enter border width in pixels: ")
)

gray_border_color = int(
    input("Enter grayscale border intensity (0-255): ")
)

binary_border_color = int(
    input("Enter binary border color (0 or 255): ")
)

if binary_border_color not in [0, 255]:
    print("Invalid binary border color!")
    exit()


# RGB border color

print("\nEnter RGB border color values (0-255):")

r = int(input("Red: "))
g = int(input("Green: "))
b = int(input("Blue: "))

if not (0 <= r <= 255 and
        0 <= g <= 255 and
        0 <= b <= 255):

    print("Invalid RGB values!")
    exit()


# Grayscale padding

padded_gray = cv2.copyMakeBorder(
    gray_img,
    border_width,
    border_width,
    border_width,
    border_width,
    cv2.BORDER_CONSTANT,
    value=gray_border_color
)


# Binary padding

padded_binary = cv2.copyMakeBorder(
    binary_img,
    border_width,
    border_width,
    border_width,
    border_width,
    cv2.BORDER_CONSTANT,
    value=binary_border_color
)


# RGB padding

padded_rgb = cv2.copyMakeBorder(
    rgb_img,
    border_width,
    border_width,
    border_width,
    border_width,
    cv2.BORDER_CONSTANT,
    value=(r, g, b)
)


# Display padded images

plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.imshow(rgb_img)
plt.title("Original RGB")
plt.axis("off")

plt.subplot(3, 2, 2)
plt.imshow(padded_rgb)
plt.title("Padded RGB")
plt.axis("off")

plt.subplot(3, 2, 3)
plt.imshow(gray_img, cmap="gray")
plt.title("Original Grayscale")
plt.axis("off")

plt.subplot(3, 2, 4)
plt.imshow(padded_gray, cmap="gray")
plt.title("Padded Grayscale")
plt.axis("off")

plt.subplot(3, 2, 5)
plt.imshow(binary_img, cmap="gray")
plt.title("Original Binary")
plt.axis("off")

plt.subplot(3, 2, 6)
plt.imshow(padded_binary, cmap="gray")
plt.title("Padded Binary")
plt.axis("off")

plt.tight_layout()
plt.show()

gray_complement = 255 - gray_img

binary_complement = 255 - binary_img


# Display complements

plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(gray_img, cmap="gray")
plt.title("Original Grayscale")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(gray_complement, cmap="gray")
plt.title("Grayscale Complement")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(binary_img, cmap="gray")
plt.title("Original Binary")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(binary_complement, cmap="gray")
plt.title("Binary Complement")
plt.axis("off")

plt.tight_layout()
plt.show()