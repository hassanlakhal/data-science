from load_image import ft_load
from pimp_image import *
import matplotlib.pyplot as plt

array = ft_load("landscape.jpg")
ft_invert(array)

ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_blue.__doc__)