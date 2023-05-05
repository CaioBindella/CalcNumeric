# from sympy import diff, Symbol

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

a = float(input('Entre com o valor 1: '))
b = float(input('Entre com o valor 2: '))
epislon = float(input('Entre com o valor E: '))

x_0 = 4
fn = 1
fln = 0
interections = 0

def CalcFunc(x):
    return ((x**3) - (2*(x**2)) - 5)

def CalcDeriv(x):
    return ((3*(x**2)) - (4*(x)))

def CalcXn1(x , y, z):
    return (x - (y/z))


def CalcXn(x , y, z):
    return (x - (y/z))

# x = Symbol('x')
# flx = ((x**3) - 2*(x**2) - 5)
# diff(flx, x)


VarXf = np.linspace(a-1, b+1, 100)
VarYf = VarXf**3 - 2*(VarXf**2) - 5

a = CalcFunc(a)
b = CalcFunc(b)
flx = CalcDeriv(x_0)

Xn1 = CalcXn(x_0, b, flx)

Xn = Xn1


while fn > epislon:
    #calcula f(xn)
    fn = CalcFunc(Xn)

    #calcula fLinha(xn)
    fln = CalcDeriv(Xn)
    
    Xn = CalcXn(Xn, fn, fln)
    interections = interections + 1
    

print(f'Valor da F(x) = {fn}')
print(f'Valor da F(x)linha = {fln}')
print(f"iterections = {interections}")

plt.grid()
plt.plot(VarXf, VarYf)
plt.xlabel('x')
plt.ylabel('y')
plt.show()