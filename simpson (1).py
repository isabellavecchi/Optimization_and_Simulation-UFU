# https://en.wikipedia.org/wiki/Simpson%27s_rule

from math import log, sin, pi

def simpson_1_3(f, a, b):
    return (b-a)/6*(f(a) + 4*f((a+b)/2) + f(b))

def simpson_3_8(f, a, b):
    return (b-a)/8*(f(a) + 3*f((2*a+b)/3) + 3*f((a+2*b)/3) + f(b))

print("caso 1")
f = lambda x: x**2 + 1
lim = [0, 2]
resp = 14/3
calc = simpson_1_3(f, *lim)
print(calc, "erro:", abs(resp-calc))
calc = simpson_3_8(f, *lim)
print(calc, "erro:", abs(resp-calc))

print("caso 2")
f = lambda x: (2*x**5 - x + 3)/x**2
lim = [1, 2]
resp = 9 - log(2)
calc = simpson_1_3(f, *lim)
print(calc, "erro:", abs(resp-calc))
calc = simpson_3_8(f, *lim)
print(calc, "erro:", abs(resp-calc))

print("caso 3")
f = lambda x: x**0.5*(x-2)
lim = [0, 4]
resp = 32/15
calc = simpson_1_3(f, *lim)
print(calc, "erro:", abs(resp-calc))
calc = simpson_3_8(f, *lim)
print(calc, "erro:", abs(resp-calc))

print("caso 4")
f = lambda x: sin(x)**2 - 1
lim = [0, pi]
resp = -pi/2
calc = simpson_1_3(f, *lim)
print(calc, "erro:", abs(resp-calc))
calc = simpson_3_8(f, *lim)
print(calc, "erro:", abs(resp-calc))
