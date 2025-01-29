import numpy as np

def ponto():
    x = 2*np.random.random() - 1
    y = 2*np.random.random() - 1
    return x, y

def dentro(p):
    return (p[0]**2 + p[1]**2)**0.5 <= 1

Ntotal = 5000

result = list()
for _ in range(100):
    Ncirc = 0
    for _ in range(Ntotal):
        if dentro(ponto()):
            Ncirc += 1
    result.append(4*Ncirc/Ntotal)

print(f"Meu π vale: {np.mean(result):.6f}")