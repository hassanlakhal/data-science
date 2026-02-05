from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np 

def rgb2gray(rgb):
    return np.dot(rgb,[0.299, 0.587, 0.144])

img = ft_load("animal.jpeg")

# print(type(img))
# imgplot = plt.imshow(img)
img2gray = rgb2gray(img)

zoom = img2gray[:3]
print(np.shape(zoom))
# img_gray = plt.imshow(zoom, cmap='gray')

plt.show()