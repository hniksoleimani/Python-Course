import imageio
import os

images = []

for file_name in sorted(os.listdir('test_images')):
    print(file_name)
    img = imageio.imread('test_images' + '/' + file_name)

imageio.mimsave('fun.gif', images)
