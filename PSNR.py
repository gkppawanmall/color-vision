from math import log10, sqrt
import cv2
import pandas as pd
import numpy as np
from skimage.color import rgb2gray
from skimage import io

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def main():
    # load the RGB image
    rgb_image5 = io.imread('o_image5.jpg')
    rgb_image9 = io.imread('o_image9.jpg')
    rgb_image43 = io.imread('o_image43.jpg')
    rgb_image46 = io.imread('o_image46.jpg')
    rgb_image51 = io.imread('o_image51.jpg')
    # convert the RGB image to grayscale using the luminosity method
    gray_image5 = rgb2gray(rgb_image5)
    gray_image9 = rgb2gray(rgb_image9)
    gray_image43 = rgb2gray(rgb_image43)
    gray_image46 = rgb2gray(rgb_image46)
    gray_image51 = rgb2gray(rgb_image51)
    #
    re_image5 = io.imread('r_image5.jpeg')
    re_image9 = io.imread('r_image9.jpeg')
    re_image43 = io.imread('r_image43.jpeg')
    re_image46 = io.imread('r_image46.jpeg')
    re_image51 = io.imread('r_image51.jpeg')
    # s
    #
    s_image5 = io.imread('s_image5.jpeg')
    s_image9 = io.imread('s_image9.jpeg')
    s_image43 = io.imread('s_image43.jpeg')
    s_image46 = io.imread('s_image46.jpeg')
    s_image51 = io.imread('s_image51.jpeg')

    value_rs5 = PSNR(rgb_image5, s_image5)
    value_rr5 = PSNR(rgb_image5, re_image5)

    value_rs9 = PSNR(rgb_image5, s_image9)
    value_rr9 = PSNR(rgb_image9, re_image9)

    value_rs43 = PSNR(rgb_image43, s_image43)
    value_rr43 = PSNR(rgb_image43, re_image43)

    value_rs46 = PSNR(rgb_image46, s_image46)
    value_rr46 = PSNR(rgb_image46, re_image46)

    value_rs51 = PSNR(rgb_image51, s_image51)
    value_rr51 = PSNR(rgb_image51, re_image51)
    # intialise data of lists.
    data = {'Sample': ['Sample-1', 'Sample-2','Sample-3','Sample-4','Sample-5'],'PSNR(orignal-Recolor)': [value_rs5, value_rs9,value_rs43,value_rs46,value_rs51],
            'PSNR(orignal-CVD Simulated)': [value_rr5,value_rr9,value_rr43,value_rr46,value_rr51]}

    # Create DataFrame
    df = pd.DataFrame(data)
    df.index = df.index + 1

    # Print the output.
    print(df)
if __name__ == "__main__":
    main()
