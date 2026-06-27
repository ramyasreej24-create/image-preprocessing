import cv2
import numpy as np
import utils

def apply_blur(image,ksize):
    if ksize % 2 == 0:
        image += 1
    return cv2.GaussianBlur(image,(ksize,ksize),0)

def apply_sharpness(image,alpha):
    blurred=cv2.GaussianBlur(image,(0,0),3)
    sharpened=cv2.addWeighted(image,1+alpha,blurred,-alpha,0)
    return sharpened

def apply_brightness(image,beta):
    return cv2.convertScaleAbs(image,alpha=1,beta=beta)

def adjust_contrast(image,alpha):
    return cv2.convertScaleAbs(image,alpha=alpha,beta=0)

def apply_edge_detection(image,t1,t2):
    edges=cv2.Canny(image,t1,t2)
    return cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)

def apply_convert_grayscale(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
