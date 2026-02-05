from PIL import Image
import numpy as np
import array


def ft_load(path: str) -> array:
    pxl = []
    try:
        img = Image.open(path)
       
        if img.format == 'JPEG':
            pxl = np.array(img)
            print(f"The shape of image is:  {np.shape(pxl)}")
        else:
            print("Only JPG and JPEG formats are supported.")
    except Exception:
        print(f"Error while processing file: {path}")

    return pxl

# print(ft_load("landscape.j5pg"))