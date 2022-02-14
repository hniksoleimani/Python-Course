import cv2
import numpy as np


#---------------------------------------------------------------------------------------------------------------------

def mean():
    images=[]
    for i in range(0,15):
        img=cv2.imread(f"/home/ali/hani/Learning/Session21/Session22/Assignment22/highway/h{i}.jpg",0)
        images.append(img)
        rows,cols=img.shape
    result=np.zeros((rows,cols), dtype="uint8")
    for image in images:
        result+=image//15
    return(result)

#---------------------------------------------------------------------------------------------------------------------

out=mean()
cv2.imwrite("Output.jpg",out)
