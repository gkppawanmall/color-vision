from os import listdir

import cv2 as cv
import files as files
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def apply_gamma(v):
    if v <= 0.0031308:
        v_prime = v * 3294.6
    elif v > 0.0031308:
        v_prime = 255 * (1.055 * (v ** 0.41666) - 0.055)
    elif v < 0:
        v_prime = v * 3294.6
    return v_prime


def remove_gamma(v):
    if v <= 0.04045 * 255:
        v_prime = v / (255 * 12.92)
    elif v > 0.04045 * 255:
        v_prime = (((v / 255) + 0.055) / 1.055) ** 2.4
    return v_prime


t_rgb_xyz = np.array(
    [[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750], [0.0193339, 0.1191920, 0.9503041]])

t_xyz_lms = np.array([[0.4002, 0.7076, -0.0808], [-0.2263, 1.1653, 0.0457], [0, 0, 0.9182]])

t_rgb_lms = t_rgb_xyz.dot(t_xyz_lms)
t_lms_rgb = np.linalg.inv(t_rgb_lms)
T = t_xyz_lms.dot(t_rgb_xyz)
print(T)

blue_lms = T.dot([[0],[0],[1]])
# print(blue_lms)


white_lms = T.dot([[1],[1],[1]])
# print(white_lms)

q1 = ((blue_lms[0] * white_lms[2]) - (white_lms[0] * blue_lms[2])) / ((blue_lms[1] * white_lms[2]) - (white_lms[1] * blue_lms[2]))
print(q1)

q2 = ((blue_lms[0] * white_lms[1]) - (white_lms[0] * blue_lms[1])) / ((blue_lms[2] * white_lms[1]) - (white_lms[2] * blue_lms[1]))
print(q2)

t_sim = np.array([[0,1.05118294,-0.05116099],[0,1,0],[0,0,1]])

path = 'E:\\PycharmProjects\\CVD\\dataset_original_images\\dataset_original_images\\'
imagesList = listdir(path)
print(imagesList)

imagesList1 = imagesList[:10]
imagesList2 = imagesList[50:60]
print(imagesList2)

for everyimage in imagesList2:
    image_name = everyimage
    try_image = cv.imread(path + everyimage)
    image_array = np.array(try_image)
    image_array = np.asfarray(image_array)
    dimension = list()
    dimension = image_array.shape
    for i in range(dimension[0]):
        for j in range(dimension[1]):
            pixel_array = np.array(image_array[i][j])
            image_array = np.asfarray(image_array)
            np.resize(pixel_array, (3, 1))
            pixel_array = np.asfarray(pixel_array)
            for n in range(3):
                pixel_array[n] = remove_gamma(pixel_array[n])

            pixel_array = t_rgb_xyz.dot(pixel_array)
            pixel_array_o = pixel_array
            pixel_array = t_xyz_lms.dot(pixel_array)
            pixel_array = t_sim.dot(pixel_array)

            for x in range(3):
                if pixel_array[x] < 0:
                    pixel_array[x] = 0
                elif pixel_array[x] > 1:
                    pixel_array[x] = 1
            image_array[i][j] = pixel_array
    plt.imsave('file_{0}_.jpeg'.format(image_name), image_array)

    #with open('file_{0}_.jpeg'.format(image_name)):

#recolor
import math
from os import listdir
import matplotlib.pyplot as plt
import cv2 as cv

path = 'E:\\PycharmProjects\\CVD\\comprasion_data\\dataset_original_images\\dataset_original_images\\'
imagesList = listdir(path)
print(imagesList)

imagesList1 = imagesList[:10]
imagesList2 = imagesList[390:400]
print(imagesList2)

for everyimage in imagesList2:
    image_name = everyimage
    try_image = cv.imread(path + everyimage)
    image_array = np.array(try_image)
    image_array = np.asfarray(image_array)
    dimension = list()
    dimension = image_array.shape
    for i in range(dimension[0]):
        for j in range(dimension[1]):
            pixel_array = np.array(image_array[i][j])
            image_array = np.asfarray(image_array)
            np.resize(pixel_array, (3, 1))
            pixel_array = np.asfarray(pixel_array)
            for n in range(3):
                pixel_array[n] = remove_gamma(pixel_array[n])

            pixel_array = t_rgb_xyz.dot(pixel_array)
            pixel_array_o = pixel_array
            pixel_array = t_xyz_lms.dot(pixel_array)
            pixel_array = t_sim.dot(pixel_array)
            pixel_array_s = pixel_array
            E_x = abs(pixel_array_o[0] - pixel_array_s[0])
            E_z = abs(pixel_array_o[2] - pixel_array_s[2])
            theta_o = math.atan(pixel_array_o[2] / pixel_array_o[0])
            theta_s = math.atan(pixel_array_s[2] / pixel_array_s[0])
            phi = abs(theta_o - theta_s)
            s, c = np.sin(phi), np.cos(phi)
            t_rotation = np.array([[s, c], [c, -s]])
            E = np.array([[E_x], [E_z]])
            E_bar = t_rotation.dot(E)
            pixel_array_s[0] = pixel_array_o[0] + E_bar[0][0]
            pixel_array_s[1] = pixel_array_o[1]
            pixel_array_s[2] = pixel_array_o[2] + E_bar[0][0] + E_bar[1][0]
            pixel_array_s = t_lms_rgb.dot(pixel_array_s)
            for x in range(3):
                if pixel_array_s[x] < 0:
                    pixel_array_s[x] = 0
                elif pixel_array_s[x] > 1:
                    pixel_array_s[x] = 1
            image_array[i][j] = pixel_array_s
    plt.imsave('recoloured_{0}'.format(image_name), image_array)

    with open('recoloured_{0}'.format(image_name)):

        files.download('recoloured_{0}'.format(image_name))
# xyz values of image as perceived by the color blind
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
i = "E:\\PycharmProjects\\CVD\\comprasion_data\\dataset_original_images\\dataset_original_images\\image9.jpg"
test_image1 = Image.open(i)
image_array1 = np.array(test_image1)
image_array1 = np.asfarray(image_array1)
dimension1 = list()
dimension1 = image_array1.shape

plt.imshow(mpimg.imread(i))

for i in range(dimension1[0]):
    for j in range(dimension1[1]):
        pixel_array1 = np.array(image_array1[i][j])
        image_array1 = np.asfarray(image_array1)
        np.resize(pixel_array1, (3, 1))
        pixel_array1 = np.asfarray(pixel_array1)
        for n in range(3):
            pixel_array1[n] = remove_gamma(pixel_array1[n])

        pixel_array1 = t_rgb_xyz.dot(pixel_array1)
        pixel_array1 = t_xyz_lms.dot(pixel_array1)
        pixel_array1 = t_sim.dot(pixel_array1)
        for x in range(3):
            if pixel_array1[x] < 0:
                pixel_array1[x] = 1 - pixel_array1[x]
        image_array1[i][j] = pixel_array1

print(image_array1[0][0])
plt.imshow(image_array1, interpolation='nearest')
plt.show()
# xyz values as perceived by normal people

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math

i = 'E:\\PycharmProjects\\CVD\\comprasion_data\\dataset_original_images\\dataset_original_images\\image9.jpg'
test_image2 = Image.open(i)
image_array2 = np.array(test_image2)
image_array2 = np.asfarray(image_array2)
dimension2 = list()
dimension2 = image_array2.shape

# plt.imshow(mpimg.imread(i))


for i in range(dimension2[0]):
    for j in range(dimension2[1]):
        pixel_array2 = np.array(image_array2[i][j])
        image_array2 = np.asfarray(image_array2)
        np.resize(pixel_array2, (3, 1))
        pixel_array2 = np.asfarray(pixel_array2)
        # if(pixel_array2[2]<=pixel_array2[0]/1.5 and pixel_array2[1]<=pixel_array2[0]/1.5):
        for n in range(3):
            pixel_array2[n] = remove_gamma(pixel_array2[n])

        pixel_array2 = t_rgb_xyz.dot(pixel_array2)
        pixel_array2_o = pixel_array2

        pixel_array2 = t_xyz_lms.dot(pixel_array2)
        pixel_array2 = t_sim.dot(pixel_array2)
        pixel_array2_s = pixel_array2
        E_x = abs(pixel_array2_o[0] - pixel_array2_s[0])
        E_z = abs(pixel_array2_o[2] - pixel_array2_s[2])
        theta_o = math.atan(pixel_array2_o[2] / pixel_array2_o[0])
        theta_s = math.atan(pixel_array2_s[2] / pixel_array2_s[0])
        phi = abs(theta_o - theta_s)
        s, c = np.sin(phi), np.cos(phi)
        t_rotation = np.array([[s, c], [c, -s]])
        E = np.array([[E_x], [E_z]])
        E_bar = t_rotation.dot(E)
        pixel_array2_s[0] = pixel_array2_o[0] + E_bar[0][0]
        pixel_array2_s[1] = pixel_array2_o[1]
        pixel_array2_s[2] = pixel_array2_o[2] + E_bar[0][0] + E_bar[1][0]
        pixel_array2_s = t_lms_rgb.dot(pixel_array2_s)
        # for n in range(3):
        # pixel_array2_s[n] = apply_gamma(pixel_array2_s[n])
        image_array2[i][j] = pixel_array2_s

print(image_array2[0][0])
plt.imshow(image_array2, interpolation='nearest')
plt.show()
