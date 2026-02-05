from load_image import ft_load
import matplotlib.pyplot as plt 


img = ft_load("animal.jpeg")
print(type(img))
imgplot = plt.imshow(img)
plt.show()