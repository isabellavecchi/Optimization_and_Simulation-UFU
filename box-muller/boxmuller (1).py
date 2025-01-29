#Aluna: Isabella Vecchi Ferreira
#Matrícula: 11621ECP002

import numpy as np
import matplotlib.pyplot as plt

rdDist = []
for i in range(1000):
    u1 = np.random.uniform(0,1)
    u2 = np.random.uniform(0, 1)
    z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
    rdDist.append(z1)
    rdDist.append(z2)

# plotar o histograma dos valores gerados
plt.hist(rdDist, bins=100)
plt.xlim(-3, 3)  # para dar "zoom"
plt.show()
