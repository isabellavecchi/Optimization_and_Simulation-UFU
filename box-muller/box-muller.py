#Aluna: Isabella Vecchi Ferreira
#Matrícula: 11621ECP002

import numpy as np
import matplotlib.pyplot as plt

rdDist = []
tam = 1000
erro = 0.05
media = 0
desvioPadrao = 1

# o PNRG uniforme utilizado foi a funcao random.rand do numpy,
# que já garante a aleatoriedade distribuída, assim como no
# arquivo prng.py
u1 = np.random.rand(tam)
u2 = np.random.rand(tam)

r = np.sqrt(-2*np.log10(u1))
theta = 2*np.pi*u2

x = r*np.cos(theta)
y = r*np.sin(theta)

# plotar o histograma dos valores antes de box-muller
plt.hist((u1,u2), bins=100)
plt.xlim(-3, 3)  # para dar "zoom"
plt.title("antes da distribuicao")
plt.show()

# plotar o histograma dos valores depois de box-muller
plt.hist((x,y), bins=100)
plt.xlim(-3, 3)  # para dar "zoom"
plt.title("depois da distribuicao")
plt.show()


print("desvio padrao de x: ", np.std(x))
print("media de x: ", np.mean(x))
print("desvio padrao de y: ", np.std(y))
print("media de y: ", np.mean(y))

def getPNRG(npArray, media, desvioPadrao):
    # while ((abs(np.std(npArray) - desvioPadrao) > erro) or (abs(np.mean(npArray) - media) > erro)):
    npArray = media + (npArray - np.mean(npArray))*(desvioPadrao/np.std(npArray))
    return npArray

x = getPNRG(x, media, desvioPadrao)
y = getPNRG(y, media, desvioPadrao)

print("desvio padrao de x: ", np.std(x))
print("media de x: ", np.mean(x))
print("desvio padrao de y: ", np.std(y))
print("media de y: ", np.mean(y))



# plotar o histograma dos valores gerados depois do conserto do desvio padrao e media
plt.hist((x,y), bins=100)
plt.xlim(-3, 3)  # para dar "zoom"
plt.title("depois da distribuicao com desvio padrao e media corretos")
plt.show()