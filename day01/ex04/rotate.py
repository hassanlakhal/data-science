from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
import sys 

def rgb2gray(rgb):
    return np.dot(rgb,[0.299, 0.587, 0.144])


def main():
    try:
        img = ft_load("animal.jpeg")
        img2gray = rgb2gray(img)
        print(img)

        h, w = np.shape(img2gray)
        zw, zh = 400, 400
        eh = round((h  - zh) // 2)
        ew = round((w - zw) // 2)

        zoom = img2gray[eh:eh + zh, ew:ew + zw]
        rotate_img = np.transpose(zoom)
        print(f"New shape after Transpose:  {np.shape(rotate_img)}")
        print(rotate_img)

        img_gray = plt.imshow(rotate_img, cmap='gray')
        plt.show()
    except Exception as e:
        exit(f"Exception {e}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(130)