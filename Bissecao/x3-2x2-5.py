import math
import matplotlib.pyplot as plt
import numpy as np

a = float(input('Entre com o valor 1: '))
b = float(input('Entre com o valor 2: '))
epislon = float(input('Entre com o valor E: '))
funcao = "(x**3 - 2*(x**2) - 5)"

Ainicial = a
Binicial = b
count = 0
tol = 0

def Calc(x):
    return (eval(funcao))

def CalcTol(x, y):
    return (abs(y - x)) 
    

inter = 0
f_a = Calc(a)
f_b = Calc(b)

VarXf = np.linspace(a-1, b+1, 1000)
VarYf = VarXf**3 - 2*(VarXf**2) - 5

tol = CalcTol(a, b)

while(tol > epislon):
    #Calcula xn
    x_n = (b + a)/2
    #Calcula f xn
    f_x_n = Calc(x_n)

    if(((f_x_n) * (f_a)) < 0):
        b = x_n
    else:
        a = x_n

    inter = inter + 1
    tol = CalcTol(a, b)        

    print(f'Iteracao {inter:.1f}')
    print(f'Valor de a= {a:.4f}')
    print(f'Valor de b= {b:.4f}')


plt.grid()
plt.scatter(a, Calc(a), c='black')
plt.scatter(b, Calc(b), c='black')
#################
plt.scatter(Ainicial, Calc(Ainicial), c='brown')
plt.scatter(Binicial, Calc(Binicial), c='brown')
#################
plt.title('Grafico Bissecao' + funcao)
plt.plot(VarXf, VarYf, c='green')
#################
plt.xlabel('x')
plt.ylabel('y')
plt.show()