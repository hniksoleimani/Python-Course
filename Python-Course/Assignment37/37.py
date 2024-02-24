import cv2
import os

img = cv2.imread("./mnist.png",0)
j, k = img.shape
j = 100
for i in range(0,10):

    if not os.path.exists(f"./{i}"):
        os.makedirs(f"./{i}")
    for x in range(0,j,20):
        for y in range(0,k,20):
            cv2.imwrite(f"./{i}/img{x}_{y}.png",img[x+(i*100):x+(i*100)+20,y:y+20])

