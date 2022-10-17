import cv2
import numpy as np
image = cv2.imread('./Assignment25/flower_input.jpg', 0)
image_normalized = image/255
result = np.zeros(image.shape)
rows, cols = image.shape
mask2 = np.ones((21,21), dtype = 'uint8')
mask2 = mask2/441
mask = np.zeros((rows,cols), dtype='uint8')
for i in range(rows):
    for j in range(cols):
        if image[i,j] > 180:
            mask[i,j] = 1
image = image/255
for i in range(10, rows-10):
    for j in range(10, cols-10):
            small_image = image_normalized[i-10:i+11,j-10:j+11]
            result[i,j] = np.sum(mask2*small_image)
result = (image*mask)+(1-mask)*result
result = result*255
img = cv2.imwrite('./output/1.jpg',result)

