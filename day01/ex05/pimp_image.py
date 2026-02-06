import array
import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array) -> array:
    invert = 255 - array
    # img2invert = plt.imshow(invert)
    # plt.show()
    return invert
#your code here
def ft_red(array) -> array:
    red = array * np.array([1,0,0])
    # img2red = plt.imshow(red)
    # plt.show()
    return red
#your code here
def ft_green(array) -> array:
    green_img = np.empty_like(array)
    
    green_img[:,:,0] = array[:,:,0] - array[:,:,0]
    
    green_img[:,:,1] = array[:,:,1]
    
    green_img[:,:,2] = array[:,:,2] - array[:,:,2]
    # img2green = plt.imshow(green_img)
    # plt.show()

#your code here
def ft_blue(array) -> array:
    blue_img = np.empty_like(array)
    
    blue_img[:,:,0] = 0
    
    blue_img[:,:,1] = 0
    
    blue_img[:,:,2] = array[:,:,2]
    # img2blue = plt.imshow(blue_img)
    # plt.show()

#your code here
def ft_grey(array) -> array:
    combined_sum = np.sum(array, axis=2)
    grey_channel = combined_sum / 3
    res = np.stack([grey_channel, grey_channel, grey_channel], axis=2).astype(np.uint8)
    print(res)
    plt.imshow(res)
    plt.show()
