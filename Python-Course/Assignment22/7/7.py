import cv2
from matplotlib.pyplot import colormaps
import numpy as np
import random

#---------------------------------------------------------------------------------------------------------------------
def noise(image):
    rows, cols= img1.shape
    noise=np.random.rand(rows,cols)
    result=(image//2)+((noise*255)//2)
    return(result)

#---------------------------------------------------------------------------------------------------------------------

img1=cv2.imread("/home/ali/hani/Learning/Session21/Session22/Picture2.jpg",0)
varr=noise(img1)

#---------------------------------------------------------------------------------------------------------------------

cv2.imwrite("output.jpg",varr)

