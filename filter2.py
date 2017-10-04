# coding: utf-8
import os
import sys
import cv2

def filter(filename):
    args = sys.argv
    image = cv2.imread(filename)
    height, width, channels = image.shape[:3]

    image = image[26:height-31, 0:width]
    height, width, channels = image.shape[:3]

    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for i in range(40, height-50):
        for j in range(width):
            hsvImage[i, j, 2] = 255 - hsvImage[i, j, 2]

    image = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)

    dirname = "output"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    cv2.imwrite(os.path.join(dirname, filename), image);

args = sys.argv
for filename in args[1:]:
    filter(filename)

