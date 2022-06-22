import os
import imageio.v2
files = os.listdir('img')
# print(files)
images = []
for i in range(len(files)):
    print(files[i])
    image = imageio.v2.imread('img/' + files[i])
    images.append(image)

imageio.mimsave('myArt.gif', images)

