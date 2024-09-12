import cv2 as c
#Crop an image
img=c.imread('images/planet_glow.jpg')
startRow=155
endRow=315
startCol=440
endCol=596
ROI=img[startRow:endRow, startCol:endCol]
ROI2=img[152:295, 211:446]
c.imshow('orginal image',img)
c.imshow('cropping',ROI)
c.imshow('cropping2',ROI2)
c.waitKey()
c.destroyAllWindows()