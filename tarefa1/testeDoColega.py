import numpy as np
import matplotlib.pyplot as plt

def dfdf(f, t):
    h = 2**-20 # 10**-12
    return (f(t+h) + f(t-h)-2*f(t))/((h**2))

t = np.linspace(0, 2*np.pi, 100)
print(t)

fun = lambda t : np.sin(t)
plt.plot(t, fun(t), 'b', label="seno")
plt.plot(t, dfdf(fun, t), 'r', label="derivada2A")
plt.legend()
plt.show()