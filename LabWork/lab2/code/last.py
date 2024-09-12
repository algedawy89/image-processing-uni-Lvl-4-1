import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('images/balloons.jpg')
# Convert BGR image to RGB
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
width = image_rgb.shape[1]
height = image_rgb.shape[0]
tx = 100

ty=70
# Translation matrix
translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
# warpAffine does appropriate shifting given the Translation matrix.
translated_image = cv2.warpAffine(image_rgb, translation_matrix, (width, height))
fig, axs = plt.subplots(1, 2, figsize=(7, 4))# Create subplots
axs[0].imshow(image_rgb)
axs [0].set_title('Original Image')
# Plot the transalted image
axs [1].imshow(translated_image)
axs[1].set_title('Image Translation')
plt.show()