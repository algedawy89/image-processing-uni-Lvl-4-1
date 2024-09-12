
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('images/balloons.jpg')
# Convert BGR image to RGB
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Image rotation parameter
center = (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2)
# getRotationMatrix2D creates a matrix needed for transformation.
rotation_matrix = cv2.getRotationMatrix2D(center, 30, 0.7)
rotation_matrix2 = cv2.getRotationMatrix2D(center, 30, 1)
# We want matrix for rotation w.r.t center to 30 degree without scaling.
rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (img.shape[1], img.shape[0]))
rotated_image2 = cv2.warpAffine(image_rgb, rotation_matrix2, (img.shape[1], img.shape[0]))
# Create subplots
fig, axs = plt.subplots(1,3, figsize=(14,4))
axs [0].imshow(image_rgb)# Plot the original image
axs[0].set_title('Original Image')
axs [1].imshow(rotated_image)# Plot the Rotated image
axs[1].set_title('Image Rotation')
axs[2].imshow(rotated_image2)
axs [2].set_title('Image Rotation2')
plt.show()