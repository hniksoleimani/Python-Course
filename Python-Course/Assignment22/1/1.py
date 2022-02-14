import cv2
import numpy as np

#-------------------------------------------------------

def subtract(image1,image2):
    img2_=255-img2
    result=(img1+img2_)
    return(result)

#-------------------------------------------------------

img1=cv2.imread("./Assignment22/a.tif",0)
img2=cv2.imread("./Assignment22/b.tif",0)
print(img1.shape)
print(img2.shape)
varr=subtract(img1,img2)

#-------------------------------------------------------

cv2.imwrite("Output.jpg",varr)


