import cv2 as c
img=c.imread("images/home.jpg") #read an image
#print(img)
c.imshow("image1", img) #display an image
c.waitKey(0)
c.imwrite("images/home.png", img) #save an image
c.destroyAllWindows()