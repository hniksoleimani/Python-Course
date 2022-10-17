import cv2
import numpy as np
image = cv2.imread('./Assignment25/building.tif', 0)
image_normalized = image/255
result = np.zeros(image.shape)
rows, cols = image.shape
mask = np.array([[-1, 0, 1]
                 ,[-1, 0, 1]
                 ,[-1, 0, 1]])
mask2 = np.array([[-1, 1, 1]
                 ,[0, 0, 0]
                 ,[1, 1, 1]])
for i in range(1, rows-1):
    for j in range(1, cols-1):
            small_image = image[i-1:i+2,j-1:j+2]
            result[i,j] = np.sum(mask2*small_image)
img = cv2.imwrite('./output/3_2.jpg',result)

