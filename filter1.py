# coding: utf-8
import os
import sys
import cv2

def filter(filename):
    args = sys.argv
    image = cv2.imread(filename)
    height, width, channels = image.shape[:3]

    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for i in range(17, height-77):
        for j in range(20, width-107):
            if hsvImage[i, j ,2] < 100:
                hsvImage[i, j] = [0, 0, 255]

    image = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)

    dirname = "output"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    cv2.imwrite(os.path.join(dirname, filename), image);

args = sys.argv
for filename in args[1:]:
    filter(filename)

