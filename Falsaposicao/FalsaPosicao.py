import math
import matplotlib.pyplot as plt
import numpy as np

RaizK = 0

def Calc(x):
    return (x**3 - 3*(x**2) - 1)

def Fake(a, b, epsilon, max_iter):
    x_k_1 = a
    x_k = b
    count = 0
    
    while abs(Calc(x_k)) > epsilon and count < max_iter:
        x_k_2 = x_k - (Calc(x_k) * (x_k - x_k_1)) / (Calc(x_k) - Calc(x_k_1))
        x_k_1 = x_k
        x_k = x_k_2
        count += 1
    
    if count == max_iter:
        print("Não foi possível encontrar uma raiz dentro do número máximo de iterações")
    else:
        print(f"A raiz é: {x_k} após {count} iterações")
        return RaizK

a = float(input('Entre com o valor 1: '))
b = float(input('Entre com o valor 2: '))
epsilon = float(input('Entre com o valor E: '))
max_iter = int(input('Entre com o número máximo de iterações: '))

RaizK = Fake(a, b, epsilon, max_iter)

VarXf = np.linspace(a-1, b+1, 1000)
VarYf = ((VarXf**3) - (3 * (VarXf**2)) - 1)

plt.grid()
plt.scatter(RaizK, Calc(RaizK), c='blue')
plt.plot(VarXf, VarYf, c='green')
plt.xlabel('x')
plt.ylabel('y')
plt.show()