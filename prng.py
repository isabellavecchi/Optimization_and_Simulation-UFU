# LCG - https://en.wikipedia.org/wiki/Linear_congruential_generators
import matplotlib.pyplot as plt
import time
import numpy as np

x0 = int(time.time())

def lcg(a, c, m):
    global x0
    x0 = (a*x0 + c) % m
    return x0/m

def moeda(a, c, m):
    global x0
    x0 = (a*x0 + c) % m
    return 1 if x0/m < 0.5 else 0

N = 100
rn = list(moeda( 1664525, 1013904223, 2**32 ) for _ in range(N))

esp = list()
for i, n in enumerate(rn):
    esp.append(sum(rn[0:i+1])/(i+1))

plt.plot(esp)
plt.plot((0,len(esp)),(0.5,0.5),':k')
plt.ylim((0,1))
plt.show()

# plt.hist(x)