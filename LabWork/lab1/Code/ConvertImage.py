import cv2 as c
import numpy as np

img=c.imread("images/home.jpg")
#convert the image to Gray-scale
grayimg=c.cvtColor(img,c.COLOR_BGR2GRAY)
#convert the image to binary image by using threshold
ret, binaryimg=c.threshold(grayimg, 120, 255, c. THRESH_BINARY)
#convert the image to binary image by using threshold
bwimg=np.zeros_like(grayimg)
bwimg[grayimg>140]=255 #threshold is 140
c.imshow("color image", img)
c.imwrite('./images/binary.jpg',binaryimg)
c.imshow("Gray-scale", grayimg)
c.imshow("binary image", binaryimg)
c.imshow("binary image2", bwimg)
c.waitKey(0)
c.destroyAllWindows()