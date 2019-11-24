import numpy as np
import matplotlib.pyplot as plt
import imageio
from scipy.fftpack import fft2
from scipy.fftpack import ifft2

im = plt.imread('D:\Kỳ 1 năm 4\Truyền thông đa phương tiện\BTLT-nhom6-master\Bai4\endcode_test.png')
im_size = im.shape[0] + im.shape[1] + im.shape[2]
fft_im = fft2(im)
imageio.imwrite('real.tif', fft_im.real)
imageio.imwrite('imagined.tif', fft_im.imag)