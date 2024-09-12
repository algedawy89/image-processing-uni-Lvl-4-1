
import cv2
image = cv2.imread('images/planet_glow.jpg')
# Convert BGR image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Define the scale factor
scale_factor_1 = 2.0 # Increase the size by 2 times
scale_factor_2 = 1/2.0 # Decrease the size by 2 times
# Get the original image dimensions
height, width = image_rgb.shape[:2]
# Calculate the new image dimensions
new_height = int(height * scale_factor_1)
new_width = int(width * scale_factor_1)
# Resize the image (Enlarge)
zoomed_image = cv2.resize(src =image_rgb,dsize=(new_width, new_height),
interpolation=cv2.INTER_CUBIC) #interpolation is(optionl) type of zoom in
# Calculate the new image dimensions
cv2.INTER_AREA
cv2.INTER_LINEAR
cv2.INTER_NEAREST
new_height1 = int(height * scale_factor_2)
new_width1 = int(width * scale_factor_2)
# Shrink image(zooming-out)
Shrink_image = cv2.resize(src= image_rgb,dsize =(new_width1, new_height1),
interpolation=cv2.INTER_AREA)
cv2.imshow('image',image)
cv2.imshow('zoomed image', zoomed_image)
cv2.imshow('Shrink image',Shrink_image)
cv2.waitKey()
cv2.destroyAllWindows ()