# https://en.wikipedia.org/wiki/Simpson%27s_rule

from math import log, sin, pi
import numpy as np
import matplotlib.pyplot as plt

passos = 10

def simpson_1_3(f, t, h):
    a = t
    b = t+h
    return (h/3)*(f(a) + 4*f((a+b)/2) + f(b))

def simpson_3_8(f, t, h):
    a = t
    b = t+h
    return ((b-a)/8)*(f(a) + 3*f((2*a+b)/3) + 3*f((a+2*b)/3) + f(b))

def setup(lim,passos):
    h = ((lim[1]-lim[0])/2)/passos
    t = np.linspace(lim[0], lim[1], passos, dtype=float) # .astype(float)
    return h, t

def plotaFunc(fun, intF, t, h):
    plt.plot(t, fun(t), 'b', label="funcao")
    plt.plot(t, intF(t), 'r', label="integral da funcao")
    plt.plot(t, simpson_1_3(fun, t, h), 'g', label="simpson 1/3", linewidth=4)
    plt.plot(t, simpson_3_8(fun, t, h), 'purple', label="simpson 3/8")
    plt.legend()
    plt.show()

def printaErro(f, intF, valX, h):
    resp = intF(valX)
    calc = simpson_1_3(f, valX, h)
    print("1/3", calc, "erro:", abs(resp-calc))
    calc = simpson_3_8(f, valX, h)
    print("3/8", calc, "erro:", abs(resp-calc))

def main(fun, intF, lim, passos, xValorTeste):
    h, t = setup(lim, passos)
    plotaFunc(fun, intF, t, h)
    printaErro(f, intF,xValorTeste, h)




print("caso 1")
sobe = 0

f = lambda x: x**2 + 1 + sobe
intF = lambda x: x**3/3 + (1+sobe)*x
lim = np.array([0, 2])

main(f, intF, lim, passos, lim[1])



print("\ncaso 2")
# np.where(x<0, -x, x)
sobe = 2.5

f = lambda x: (2*x**5 - x + 3)/x**2 + sobe
intF = lambda x: (x**4)/2 -np.log(abs(x)) - (3*x.astype(float)**-1) + sobe*x
lim = np.array([1, 2])

main(f, intF, lim, passos, lim[1])



print("\ncaso 3")
sobe = 2

f = lambda x: x**0.5*(x-2) + sobe
intF = lambda x: 0.4*x**2.5 - 4/3*x**1.5 + sobe*x
lim = np.array([0, 4])

lims = np.array([0, 0.4, 0.9, 4])
for xi in range(3):
    main(f, intF, [lims[xi], lims[xi+1]], passos, lims[xi+1])   
# main(f, intF, lim, passos, lim[1])



print("\ncaso 4")
sobe = 1.5

f = lambda x: np.sin(x)**2 - 1 + sobe
intF = lambda x: 1/2*x - 1/4*np.sin(2*x) + 0.5*x
lim = np.array([0, np.pi])

partes = 4
lims = np.linspace(lim[0], lim[1], partes+1)
# main(f, intF, lim, passos, lim[1])
for xi in range(partes):
    main(f, intF, [lims[xi], lims[xi+1]], passos, lims[xi+1])   