import numpy as np
import matplotlib.pyplot as plt

f = 1
fs = 8000
N = 5
pi = np.pi
A = 1

t = np.linspace(0, N/f, (N/f)*fs*1)

s2t = np.zeros(len(t))
n = 10

for i in np.arange(0, 2*n+2):
	m = 2*i +1
	s2t = s2t + (A/(m*m))*np.sin(2*m*pi*f*t)

plt.plot(t,s2t)

plt.xlabel('t')
plt.ylabel('s2(t)')
plt.title('Tin hieu s2(t)')

plt.savefig('s2t.png')