import imageio
import numpy as np
import matplotlib.pyplot as plt

def findOriginal(rscale_im, gscale_im, bscale_im, ascale_im):
    rgba = rscale_im.copy()
    rgba[:,:,1] = gscale_im[:,:,1]
    rgba[:,:,2] = bscale_im[:,:,2]
    rgba[:,:,3] = ascale_im[:,:,3]
    return 255 * rgba

rscale_im = plt.imread('red.png')
gscale_im = plt.imread('green.png')
bscale_im = plt.imread('blue.png')
ascale_im = plt.imread('alpha.png')
orrgba_im = findOriginal(rscale_im, gscale_im, bscale_im, ascale_im).astype('uint8')
imageio.imwrite('recover.png', orrgba_im)
