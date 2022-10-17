import cv2
import numpy as np




def conv(choice):                 
    if choice =='1':
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                    small_image = image_normalized[i-1:i+2,j-1:j+2]
                    result[i,j] = np.sum(mask1*small_image)
    elif choice == '2':
        for i in range(2, rows-2):
            for j in range(2, cols-2):
                    small_image = image_normalized[i-2:i+3,j-2:j+3]
                    result[i,j] = np.sum(mask2*small_image)
    elif choice == '3':
        for i in range(3, rows-3):
            for j in range(3, cols-3):
                    small_image = image_normalized[i-3:i+4,j-3:j+4]
                    result[i,j] = np.sum(mask3*small_image)
    elif choice == '4':
        for i in range(7, rows-7):
            for j in range(7, cols-7):
                    small_image = image_normalized[i-7:i+8,j-7:j+8]
                    result[i,j] = np.sum(mask4*small_image)
    else:
        print('Invalid input')



image = cv2.imread('output/lion.png', 0)
size = input('Enter[1-4]:')
image_normalized = image/255
result = np.zeros(image.shape)
print(image.shape)
rows, cols = image.shape
mask2 = np.ones((5,5), dtype = 'uint8')
mask2 = mask2/25
mask3 = np.ones((7,7), dtype='uint8')
mask3 = mask3/49
mask4 = np.ones((15,15), dtype='uint8')
mask4 = mask4/225
mask1 = np.array([[1/9, 1/9, 1/9]
                 ,[1/9, 1/9, 1/9]
                 ,[1/9, 1/9, 1/9]])

conv(size)
result = result*255
img = cv2.imwrite('./output/4_4.jpg',result)



