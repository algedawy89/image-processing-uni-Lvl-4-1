import sys
import cv2 as c
img=c.imread("images/home.jpg",0)
if img is None:
    print('Failed to read image from file')
    sys.exit(1)
c.imshow("image", img)
# if wait for any key to be pressed to excute next step
k=c.waitKey(0)
if k == 27: # wait for ESC key to exit
    c.destroyAllwindows()
elif k == ord('s'): # wait for 's' key to save and exit
    c.imwrite("images/treesgray.png", img)
    c.destroyAllWindows ()
