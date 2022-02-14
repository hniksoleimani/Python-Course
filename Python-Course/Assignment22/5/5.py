import cv2
import numpy as np

#---------------------------------------------------------------------------------------------------------------------


def mean(image1,image2):
    result=(new_img1//3+img2//3+new_img1//3)
    return(result)

#---------------------------------------------------------------------------------------------------------------------




img1=cv2.imread("/home/ali/hani/Learning/Session21/Session22/Picture2.jpg",0)
img2=cv2.imread("/home/ali/hani/Learning/Session21/Session22/khayyam.jpg",0)
new_img1=cv2.resize(img1,(185,273))
varr=mean(new_img1,img2)

#---------------------------------------------------------------------------------------------------------------------

cv2.imwrite("Output.jpg",varr)

