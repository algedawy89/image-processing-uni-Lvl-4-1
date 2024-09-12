import cv2
import numpy as np
# إنشاء صورة فارغة
image = np.zeros((500, 500, 3), dtype="uint8")
# رسم مستطيل (النقطة العلوية اليسرى: 100,100 | النقطة السفلية اليمنى: 400,400 | اللون: أخضر | السماكة: 5)
cv2.rectangle(image, (100, 100), (400, 400), (0, 255, 0), 5)
cv2.imwrite("images/rectangle_image.jpg", image)
