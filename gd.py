# https://en.wikipedia.org/wiki/Gradient_descent
# https://en.wikipedia.org/wiki/Gradient

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: (x[0]**4+x[1]**4)*0.25 - (x[0]**3+x[1]**3)/3 - (x[0]**2+x[1]**2) - 4
x = np.linspace(-2,3)
y = np.linspace(-2,3)
X, Y = np.meshgrid(x, y)



h = 10**-12
def derivparcial(f, x, d):
    a = x.copy()
    a[d] = a[d] + h
    b = x.copy()
    b[d] = b[d] - h
    return (f(a) - f(b))/(2*h)

# print(derivparcial(f,[2.1,1.8],0))
# print(derivparcial(f,[2.1,1.8],1))

gradient = lambda f, x: np.array(
    list(derivparcial(f,x,d) for d in range(x.shape[0]))
)#[:, np.newaxis]

gamma = 0.1
x = np.array([[0.5],[0.5]], dtype=float)
lop = [x]
while True:
    old = x
    x = x - gamma*gradient(f, x)
    lop.append(x)
    if np.sum(np.abs(x - old)) <= h:
        break

print(x)
print(len(lop))

if len(lop) < 100:
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot_surface(X, Y, f((X, Y)), cmap="rainbow", zorder=1)
    for xi in lop:
        ax.scatter(*(xi+0.01), f(xi), color='k', zorder=10)
    plt.show()