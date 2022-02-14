import cv2
import numpy as np

#---------------------------------------------------------------------------------------------------------------------

def edge_detection(image1):
    inverted=255-img1
    blurred= cv2.GaussianBlur(inverted, (21,21), 0)
    inverted_blurred=255-blurred
    sketch = img1 / inverted_blurred
    sketch=sketch * 255
  
#---------------------------------------------------------------------------------------------------------------------
img1=cv2.imread("/home/ali/hani/Learning/Session21/Session22/Picture2.jpg",0)
varr=edge_detection(img1)

#---------------------------------------------------------------------------------------------------------------------

cv2.imwrite("Output.jpg",varr)

