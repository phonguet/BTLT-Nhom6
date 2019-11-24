import numpy as np
import linearConvolve
import cyclicConvolve
import cyclicConvolution

inSignal = [10, 9, 8, 1, 1, 1, 12, 17, 9, 4]
impulseResponse = [0, 1, 1, 0]
print("Linear convolution ham co san: ")
print(np.convolve(impulseResponse, inSignal))
print("Linear convolution ham tu lam: ")
print(linearConvolve.linearConvolve(inSignal, impulseResponse))
print("Cyclic convolution ham tu lam: ")
print(cyclicConvolve.cyclicConvolve(inSignal, impulseResponse))
print("Cyclic convolution theo huong dan trong slide: ")
print(cyclicConvolution.cyclicConvolution(inSignal, impulseResponse))