import matplotlib.pyplot as plt
import numpy as np

a = float(input('Entre com o valor 1: '))
b = float(input('Entre com o valor 2: '))

x0 = float(input('Entre com o valor de x0: '))
x1 = float(input('Entre com o valor de x1: '))
tol = float(input('Entre com o valor E: '))

def secante(f, x0, x1, tol, max_iter):
    i = 0
    while i < max_iter:
        fx0, fx1 = f(x0), f(x1)
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        fx2 = f(x2)
        print(f'Iteracao: {i} , fxn = {fx2}')
        if abs(fx2) < tol:
            return x2
        x0, x1 = x1, x2
        i += 1
    
    raise ValueError("Número máximo de iterações excedido.")


def f(x):
    return ((x**3) - (2*(x**2)) - 5)

max_iter = 100

VarXf = np.linspace(a-1, b+1, 1000)
VarYf = ((VarXf**3) - 2*(VarXf**2) - 5)

raiz = secante(f, x0, x1, tol, max_iter)

print(f'Raiz {raiz:.4f}')

plt.grid()
plt.scatter(raiz, f(raiz), c='blue')
plt.plot(VarXf, VarYf, c='green')
plt.xlabel('x')
plt.ylabel('y')
plt.show()