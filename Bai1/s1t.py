import numpy as np
import matplotlib.pyplot as plt

f = 1
fs = 8000
N = 5
pi = np.pi
A = 1
 
t = np.linspace(0, N/f, (N/f)*fs*1) 

s1t = A*(np.sin(2*pi*f*t))
plt.figure()
plt.plot(t,s1t)

plt.xlabel('t')
plt.ylabel('s1(t)')
plt.title('Tin hieu s1(t)')

plt.savefig('s1t.png')