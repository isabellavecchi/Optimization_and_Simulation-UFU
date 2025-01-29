#Aluna: Isabella Vecchi Ferreira
#Matrícula: 11621ECP002

import numpy as np
import matplotlib.pyplot as plt

def dfdt(f, t):
    h = 2**(-32)    ##10**-12
    return (f(t+h) - f(t-h))/(2*h)

def d2fdt2(f, t):
    h = 2**(-10)
    #Com este valor, o gráfico ficou certo, acima de 2^-3, já vai ficando mais linear
    #com valores mais altos, o resultado vira uma reta
    return (f(t+h) -2*f(t) + f(t-h))/(h**2)

fun = lambda t : np.sin(t)
t = np.linspace(0, 2*np.pi, 99)
plt.plot(t, fun(t), 'b', label="seno")
plt.plot(t, dfdt(fun, t), 'r', label="1a derivada")
plt.plot(t, d2fdt2(fun, t), 'g', label="2a derivada")
plt.legend()
plt.show()