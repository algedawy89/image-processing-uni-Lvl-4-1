import cv2 as c
img=c.imread("images/home.jpg")
px=img[100,100]
print(px)
(B,G,R)=img[100,50]
print("R={} , G={} ,B={}".format(R, G,B))

# b g r the order of colors in python