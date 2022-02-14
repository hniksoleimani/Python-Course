import cv2
import numpy as np

#-------------------------------------------------------

def subtract(image1,image2):
    
    img1_=255-img1
    result=(img1_+img2)
    return(result)

#-------------------------------------------------------

img1=cv2.imread("./Assignment22/board - test.bmp",0)
img2=cv2.imread("./Assignment22/board - origin.bmp",0)
img1=cv2.flip(img1, 1)
print(img1.shape)
print(img2.shape)
varr=subtract(img1,img2)

#-------------------------------------------------------

cv2.imwrite("Output.jpg",varr)

