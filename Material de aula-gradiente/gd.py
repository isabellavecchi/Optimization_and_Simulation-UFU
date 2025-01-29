# https://en.wikipedia.org/wiki/Gradient_descent
# https://en.wikipedia.org/wiki/Gradient

import numpy as np
import matplotlib.pyplot as plt
from math import sin

f = lambda x: (x[0]**5+x[1]**5+x[2]**5)*0.2 - (x[0]**4+x[1]**4+x[2]**4)*0.25 - (x[0]**3+x[1]**3+x[2]**3)/3 - 4
x = np.linspace(-2,3)
y = np.linspace(-2,3)
z = np.linspace(-2,3)
X, Y, Z = np.meshgrid(x, y, z)



h = 10**-12
def derivparcial(f, x, d):
    a = x.copy()
    a[d] = a[d] + h
    b = x.copy()
    b[d] = b[d] - h
    return (f(a) - f(b))/(2*h)

# print(derivparcial(f,[2.1,1.8,1.9],0))
# print(derivparcial(f,[2.1,1.8,1.9],1))
# print(derivparcial(f,[2.1,1.8,1.9],2))

gradient = lambda f, x: np.array(
    list(derivparcial(f,x,d) for d in range(x.shape[0]))
)#[:, np.newaxis]

gamma = 0.01
x1 = (np.random.random()*5)-2
x2 = (np.random.random()*5)-2
x3 = (np.random.random()*5)-2
x = np.array([[x1],[x2],[x3]], dtype=float)

# print(gradient(f,x))

lop = [x]
while True:
    old = x
    x = x + gamma*gradient(f, x)
    print("ciclo: ",len(lop))
    print(x)
    lop.append(x)
    if np.sum((x - old)**2)/x.shape[0] <= 10**-6:
        break

print("x = \n",x)
print("Total de ciclos: ",len(lop))
print("F(x) = ",f(x))

# if len(lop) < 100:
#     ax = plt.figure().add_subplot(projection='3d')
#     ax.plot_surface(X, Y, Z, cmap="rainbow", zorder=1)
#     for xi in lop:
#         ax.scatter(*(xi+0.01), f(xi), color='k', zorder=10)
#     plt.show()