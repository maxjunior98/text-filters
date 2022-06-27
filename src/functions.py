import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def filter_otsu(pwd, out):
    image = cv.imread(pwd, 0)
    blur = cv.GaussianBlur(image, (5,5),0)
    ret, th = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    cv.imwrite('./pictures/results/' + out, th)

def filter_global_thresholding(pwd, th, out):
    image = cv.imread(pwd, 0)
    ret, new_img = cv.threshold(image , th, 255, cv.THRESH_BINARY)
    cv.imwrite('./pictures/results/' + out, new_img)

def filter_adaptative_gaussian(pwd, out):
    image = cv.imread(pwd, 0)
    new_img = cv.adaptiveThreshold(image ,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    cv.imwrite('./pictures/results/' + out, new_img)
    