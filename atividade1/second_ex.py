import numpy as np
import math
import matplotlib.pyplot as plt



eq_matrix = [[2,1,1,1,1],[1,2,1,1,1],[1,1,2,1,1],[1,1,1,2,1],[1,1,1,1,2]]
res_matrix = [4,5,6,7,8]

inv_matrix = np.linalg.inv(eq_matrix)
var_matrix = np.dot(inv_matrix,res_matrix)
print(var_matrix)


#2d

def sistemaVander(x,y,n):
    A = np.empty((n,n))
    b = np.empty((n))
    for i in range(0,n):
        A[i,0] = 1
        for j in range(1,n):
            A[i,j] = A[i,j-1]*x[i]
        b[i] = y[i]
    return A, b

x = np.linspace(0,2*np.pi,32)
y = np.cos(x)


a2,b2 = sistemaVander(x,y,3)
a3,b3 = sistemaVander(x,y,4)

a4,b4 = sistemaVander(x,y,5)

x2 = np.linalg.solve(a2,b2)
x3 = np.linalg.solve(a3,b3)
x4 = np.linalg.solve(a4,b4)
#
p2 = np.poly1d(x2[::-1])
p3 = np.poly1d(x3[::-1])
p4 = np.poly1d(x4[::-1])
plt.plot(x,p2(x))
plt.plot(x,p3(x))
plt.plot(x,p4(x))

plt.scatter(x,y)
plt.show()
