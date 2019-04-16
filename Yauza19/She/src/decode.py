import cv2
import numpy as np
from generateMask import *


mask = generateMatrix()

def getBit(block, mask):
    av_1 = 0
    av_0 = 0
    for i in range(8):
        for j in range(8):
            if mask[i][j] == 1:
                av_1 += getBrightness(block[i][j])
            else:
                av_0 += getBrightness(block[i][j])

    oneEntries = np.count_nonzero(mask)

    av_1 = av_1 / oneEntries
    av_0 = av_0 / (64 - oneEntries)

    if (av_0 - av_1 >= 0):
        return '1'
    elif (av_0 - av_1 < 0):
        return '0'

def getBrightness(pixel):
    #cv2 по умолчанию парсит картинки в формат GBR
    return 0.2126*pixel[2]+0.7152*pixel[1]+0.0722*pixel[0]

image = cv2.imread('she.png')

data = ""

block_img = np.zeros(image.shape)
im_h, im_w = image.shape[:2]
print(im_h, im_w)
bl_h, bl_w = 8, 8

for row in np.arange(im_h - bl_h + 1, step=bl_h):
    for col in np.arange(im_w - bl_w + 1, step=bl_w):
        data += getBit(image[row:row+bl_h, col:col+bl_w], mask)

print(data)

        
