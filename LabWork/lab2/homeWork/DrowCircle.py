import cv2
import numpy as np
# إنشاء صورة فارغة
image = np.zeros((500, 500, 3), dtype="uint8")
# رسم دائرة (المركز: 250,250 | نصف القطر: 100 | اللون: أزرق | السماكة: 5)
cv2.circle(image, (250, 250), 100, (255, 0, 0), 5)
cv2.imwrite("images/circle_image.jpg", image)

