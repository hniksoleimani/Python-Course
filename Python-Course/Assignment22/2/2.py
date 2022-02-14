import cv2
import numpy as np

#---------------------------------------------------------------------------------------------------------------------

pieces=[[],[],[],[],[],[]]
for j in range(1,5):
    for i in range(1,6):
        img=cv2.imread(f"/home/ali/hani/Learning/Session21/Session22/Assignment22/black hole/{j}/{i}.jpg",0)            
        pieces[j-1].append(img)


hole=[]

for j in range(4):
    emptyimage=np.zeros((1000,1000), dtype='uint8')
    for i in range(5):
        emptyimage+=pieces[j][i]//5
        # print(pieces[j][i])
    
    hole.append(emptyimage)
# print(len(hole[1]))

 
cv2.imwrite("/home/ali/hani/Learning/Session21/Session22/111/1212.jpg",np.concatenate((np.concatenate((hole[0], hole[2])), np.concatenate((hole[1], hole[3]))), axis=1))



       

