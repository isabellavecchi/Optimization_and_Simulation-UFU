import math
import numpy as np
import matplotlib.pyplot as plt

#A = np.array([[3,4,3],[5,-2,8],[1,3,-1]])
#b = np.array([37,42,9])

print("EXECRÍCIO 2")

################################## LETRA A ######################################
print("letra a)\n")
#np.set_printoptions(precision=2)
A = np.array([  [2,1,1,1,1],
                [1,2,1,1,1],
                [1,1,2,1,1],
                [1,1,1,2,1],
                [1,1,1,1,2]])
b = np.array([4,5,6,7,8])

A_inv = np.linalg.inv(A)

#X = A_inv*b
X = np.round_(np.dot(A_inv,b),2)
#X = np.linalg.solve(A,b)

print("v = {}\nw = {}\nx = {}\ny = {}\nz = {}".format(X[0],X[1],X[2],X[3],X[4]))
print("\n\n")

################################## LETRA B ######################################
print("letra b)")
A = np.array([  [ 0, 3,-6, 6, 4],
                [ 3,-7, 8,-5, 8],
                [ 3,-9,12,-9, 6]])
b = np.array([-5,9,15])

A_inv = np.linalg.pinv(A)
X = np.round_(np.dot(A_inv,b),2)

print("x1 = {}\nx2 = {}\nx3 = {}\nx4 = {}\nx5 = {}".format(X[0],X[1],X[2],X[3],X[4]))
print("\n\n")


################################## LETRA C ######################################
print("letra c)")
y = lambda x : np.sin(x) + np.random.random((25,))
x = np.linspace(0, 3*np.pi/5, 25)
a, b = 0, 0

def best_line(x, y):
    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    sum_y = sum(y)
    #y_ = [math.log(yi) for yi in y]
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    n = len(x)
    
    A = (n*sum_xy - sum_x*sum_y)/(n*sum_x2 - (sum_x**2))
    B = sum_y/n - A*(sum_x/n)

    return A, B

a,b = best_line(x,y(x))
print("coeficiente angular = {0:.3f}\ncoeficiente linear = {1:.3f}".format(a, b))

bline = lambda x : a*x + b

plt.plot(x, bline(x), label="ln(y)", zorder=2, color='pink', linewidth=2)
plt.scatter(x,y(x), zorder=1,s=25)
plt.legend()
plt.show()

print("\n\n")

################################## LETRA D ######################################
'''
Utilizei pinv, pois apesar de ser o menos preciso, é o que menos dá erro
pelo menos na minha máquina...
'''
print("letra d)")

def sistemaVander(grau,x,f):
    n = grau+1
    X = np.empty((n))
    A = np.empty((n,n))
    b = np.empty((n))
    rd = np.random.randint(0,32,n)

    print("Pontos:")
    #para pegar pontos aleatórios
    for i in range(0,n):
        X[i] = x[rd[i]]
    np.sort(X) #só pra ficar bonitinho

    for i in range(0,n):
        #printando os pontos
        print("({0:.2f} graus,{1:.2f})".format(X[i]*180/np.pi,f(X[i])))

        #interpolacao
        A[i,0] = 1
        for j in range(1,n):
            A[i,j] = A[i,j-1]*X[i]
        b[i] = f(X[i])

    return A, b

#só pra printar as matrizes na resposta de maneira organizada
def printAlgMatriz():
    print("\nA*x = b")
    print("\nA = ")
    print(A)
    print("\nx = ")
    print(result)
    print("\nb = ")
    print(b)

#calculo do erro absoluto
def erro(f1, f2, x):
    erro = 0
    for i in range (len(x)):
        erro += abs(f1(x[i]) - f2(x[i]))
    return erro

#funcao da questao
x = np.linspace(0, 2*np.pi, 32)
y = lambda x : np.cos(x)
A, b, X

##RESPOSTAS
#2O GRAU
print("-------Interpolacao de 2o grau-------")
result = np.empty((3))

A, b = sistemaVander(2,x,y)
A_inv = np.linalg.pinv(A)

result = np.dot(A_inv,b)
polinomio2g = np.poly1d(result[::-1])

printAlgMatriz()
print("\n\nPolinomio e erro:")
print("f(x) = {2:.2f}x^2 + {1:.2f}x + {0:.2f}".format(result[0], result[1], result[2]))
print("erro = {0:.2f}".format(erro(y, polinomio2g, x)))


#3O GRAU
print("\n\n\n-------Interpolacao de 3o grau-------")
result = np.empty((4))

A, b = sistemaVander(3,x,y)
A_inv = np.linalg.pinv(A)

result = np.dot(A_inv,b)
polinomio3g = np.poly1d(result[::-1])

printAlgMatriz()
print("\n\nPolinomio e erro:")
print("f(x) = {3:.2f}x^3 + {2:.2f}x^2 + {1:.2f}x + {0:.2f}".format(result[0], result[1], result[2], result[3]))
print("erro = {0:.2f}".format(erro(y, polinomio3g, x)))


#4O GRAU
print("\n\n\n-------Interpolacao de 4o grau-------")
result = np.empty((5))

A, b = sistemaVander(4,x,y)
A_inv = np.linalg.pinv(A)

result = np.dot(A_inv,b)
polinomio4g = np.poly1d(result[::-1])

printAlgMatriz()
print("\n\nPolinomio e erro:")
print("f(x) = {4:.2f}x^4 + {3:.2f}x^3 + {2:.2f}x^2 + {1:.2f}x + {0:.2f}".format(result[0], result[1], result[2], result[3], result[4]))
print("erro = {0:.2f}".format(erro(y, polinomio4g, x)))

##Plotando os gráficos
plt.plot(x, y(x), "black", label="cos", zorder=1, linewidth=5)
plt.plot(x, polinomio2g(x), "purple", label="interp. 2 grau", zorder=3)
plt.plot(x, polinomio3g(x), 'g', label="interp. 3 grau", zorder=2)
plt.plot(x, polinomio4g(x), 'r', label="interp. 4 grau", zorder=4)
plt.legend()
plt.show()