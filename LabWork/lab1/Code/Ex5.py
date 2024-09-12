import cv2 as c

def line(shape:str,length:int):
    [print(shape[0],end='') for _ in range(length)]
    print()

       
    
print()
img=c.imread("images/home.jpg",0)
line('*',20)
print("shape->dimensions: ",img.shape)
print("size->numbers of pixels: ",img.size)
print("Type: ",img.dtype)
line('*',20)

c.imshow("image", img)
c.waitKey(0)
c.destroyAllWindows()

print()

img2=c.imread("images/home.jpg")

print('image2')
print("shape->dimensions: ",img2.shape)
print("size->numbers of pixels: ",img2.size)
print("Type: ",img2.dtype)
line('*',20)

c.imshow("image2", img2)
c.waitKey(0)
c.destroyAllWindows()

print()







