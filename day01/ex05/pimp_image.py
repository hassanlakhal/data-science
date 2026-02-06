import array
import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    invert = 255 - array
    return invert

def ft_red(array) -> array:
    """This function keeps only the red channel of the image."""
    red = array * np.array([1,0,0])
    return red

def ft_green(array) -> array:
    """This function keeps only the green channel of the image."""
    green_img = np.empty_like(array)
    
    green_img[:,:,0] = array[:,:,0] - array[:,:,0]
    
    green_img[:,:,1] = array[:,:,1]
    
    green_img[:,:,2] = array[:,:,2] - array[:,:,2]

    return green_img 


def ft_blue(array) -> array:
    """This function keeps only the blue channel of the image."""

    blue_img = np.empty_like(array)
    
    blue_img[:,:,0] = 0
    
    blue_img[:,:,1] = 0
    
    blue_img[:,:,2] = array[:,:,2]
    return blue_img

def ft_grey(array) -> array:

    """Applies a grayscale filter to the image received."""
    combined_sum = np.sum(array, axis=2)
    grey_channel = combined_sum / 3
    res = np.stack([grey_channel, grey_channel, grey_channel], axis=2).astype(np.uint8)
    return res
