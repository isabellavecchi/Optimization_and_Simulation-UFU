import numpy as np
import matplotlib.pyplot as plt

melhor = np.argmin  #minimização
# melhor = np.argmax  #maximização
landscape = lambda x : np.sum(x**2) #minimização
limits = (-2,2)
dimension = 2
npop = 100
ngen = 50
prep = 0.80
pmut = 0.01

class Individuo:
    def __init__(self, n):
        self.genotype = \
            (limits[1]-limits[0])*np.random.random(size=(n, 1))+limits[0]
    def __repr__(self):
        return f"{self.genotype.T[0]}"
    def fitness(self, landscape):
        return landscape(self.genotype)
    def reproduction(self, other):
        genchild = np.zeros(self.genotype.shape)
        for i in range(dimension):
            r = np.random.random()
            genchild[i,0] = (1-r)*self.genotype[i,0] + r*other.genotype[i,0]
        child = Individuo(0)
        child.genotype = genchild
        return child
    def mutation(self):
        idm = np.random.randint(0, dimension)
        self.genotype[idm,0] += np.random.normal()

Population = list(Individuo(dimension) for _ in range(npop))
fitPop = lambda population : list(i.fitness(landscape) for i in population)
# def fitPop(population):
#     return list(i.fitness() for i in population)

def selection(population):
    select = list()
    fitness = fitPop(population)
    for _ in fitness:
        choices = np.random.choice(dimension, size=(3,))
        win1 = choices[melhor(list(fitness[f] for f in choices))]
        choices = np.random.choice(dimension, size=(3,))
        win2 = choices[melhor(list(fitness[f] for f in choices))]
        select.append((win1,win2))
    return select

Offspring = Population.copy()
mfit = list()
bfit = list()
# Laço de gerações
for g in range(ngen):
    for i, t in enumerate(selection(Population)):
        if np.random.random() < prep:
            Offspring[i] = Population[t[0]].reproduction(Population[t[1]])
        if np.random.random() < pmut:
            Offspring[i].mutation()
    Population = Offspring.copy()
    fp = fitPop(Population)
    mfit.append(np.mean(fp))
    bfit.append(fp[melhor(fp)])

resposta = Population[melhor(fitPop(Population))]
print(resposta)

plt.plot(mfit, 'b', label='mean')
plt.plot(bfit, 'r', label='best')
plt.legend()
plt.show()