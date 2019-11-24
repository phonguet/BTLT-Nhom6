import numpy as np
import matplotlib.pyplot as plt
import imageio

def toGray(rgba_im):
    r, g, b = rgba_im[:,:,0], rgba_im[:,:,1], rgba_im[:,:,2]
    gray = rgba_im.copy()
    gray[:,:,0] = 0.3*r + 0.59*g + 0.11*b
    gray[:,:,1] = 0.3*r + 0.59*g + 0.11*b
    gray[:,:,2] = 0.3*r + 0.59*g + 0.11*b
    gray[:,:,3] = 1
    return 255*gray

def toRed(rgba_im):
    red = rgba_im.copy()
    red[:,:,1] = 0
    red[:,:,2] = 0
    red[:,:,3] = 1
    return 255*red
    
def toGreen(rgba_im):
    green = rgba_im.copy()
    green[:,:,0] = 0
    green[:,:,2] = 0
    green[:,:,3] = 1
    return 255*green
    
def toBlue(rgba_im):
    blue = rgba_im.copy()
    blue[:,:,0] = 0
    blue[:,:,1] = 0  
    blue[:,:,3] = 1
    return 255*blue
    
def toAlpha(rgba_im):
    alpha = rgba_im.copy()
    alpha[:,:,0] = 0
    alpha[:,:,1] = 0
    alpha[:,:,2] = 0
    return 255*alpha

rgba_im = plt.imread('D:\Kỳ 1 năm 4\Truyền thông đa phương tiện\BTLT-Nhom6\Bai3\convert_test.png', 0)

gray_img = toGray(rgba_im).astype('uint8')
imageio.imwrite('gray.png', gray_img)

red_img = toRed(rgba_im).astype('uint8')
imageio.imwrite('red.png', red_img)

green_img = toGreen(rgba_im).astype('uint8')
imageio.imwrite('green.png', green_img)

blue_img = toBlue(rgba_im).astype('uint8')
imageio.imwrite('blue.png', blue_img)

alpha_img = toAlpha(rgba_im).astype('uint8')
imageio.imwrite('alpha.png', alpha_img)