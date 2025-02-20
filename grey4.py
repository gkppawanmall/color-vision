import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import io
from PIL import Image
# load the RGB image
rgb_1 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data\\16.jpg')
rgb_2 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data\\17.jpg')
rgb_3 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data\\18.jpg')
rgb_4 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data\\19.jpg')
rgb_5 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data\\20.jpg')
# convert the RGB image to grayscale using the luminosity method
gray_1 = rgb2gray(rgb_1)
gray_2 = rgb2gray(rgb_2)
gray_3 = rgb2gray(rgb_3)
gray_4 = rgb2gray(rgb_4)
gray_5 = rgb2gray(rgb_5)
#
rgb_re_1 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data_recolor\\recoloured_16.png')
rgb_re_2 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data_recolor\\recoloured_17.png')
rgb_re_3 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data_recolor\\recoloured_18.png')
rgb_re_4 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data_recolor\\recoloured_19.png')
rgb_re_5 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data_recolor\\recoloured_20.png')
#s
#
rgb_s_1 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data_simulate\\file_16.png_.jpeg')
rgb_s_2 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data_simulate\\file_17.png_.jpeg')
rgb_s_3 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data_simulate\\file_18.png_.jpeg')
rgb_s_4 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data_simulate\\file_19.png_.jpeg')
rgb_s_5 = io.imread('E:\\PycharmProjects\\CVD\\comprasion_data_simulate\\file_20.png_.jpeg')
# display the RGB and grayscale images side-by-side
fig, ax = plt.subplots(nrows=5, ncols=4)
ax[0, 0].imshow(rgb_1)
ax[0, 0].set_title('Orignal image')
ax[0, 1].imshow(gray_1, cmap='gray')
ax[0, 1].set_title('Grayscale image')
ax[0, 2].imshow(rgb_re_1)
ax[0, 2].set_title('Recolor image')
ax[0, 3].imshow(rgb_s_1)
ax[0, 3].set_title('CVD Simulated image')

ax[1, 0].imshow(rgb_2)
ax[1, 1].imshow(gray_2, cmap='gray')
ax[1, 2].imshow(rgb_s_2)
ax[1, 3].imshow(rgb_re_2)

ax[2, 0].imshow(rgb_3)
ax[2, 1].imshow(gray_3, cmap='gray')
ax[2, 2].imshow(rgb_s_3)
ax[2, 3].imshow(rgb_re_3)

ax[3, 0].imshow(rgb_4)
ax[3, 1].imshow(gray_4, cmap='gray')
ax[3, 2].imshow(rgb_s_4)
ax[3, 3].imshow(rgb_re_4)


ax[4, 0].imshow(rgb_5)
ax[4, 1].imshow(gray_5, cmap='gray')
ax[4, 2].imshow(rgb_s_5)
ax[4, 3].imshow(rgb_re_5)

plt.show()
