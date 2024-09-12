import cv2
import numpy as np

# إنشاء صورة فارغة
image = np.zeros((500, 500, 3), dtype="uint8")

# رسم خط (من النقطة: 100,100 إلى النقطة: 400,400 | اللون: أحمر | السماكة: 5)
# cv2.line((x1,y1),(x2,y2),(color=rgb),wheight)
cv2.line(image, (100, 100), (400, 400), (0, 0, 255), 5)
cv2.imwrite("images/line_image.jpg", image)
