'''
Referencia: Trabalho 3 
Nome: Juliana Guimarães de Farias 00278075
Data: 06/11/2019
Objetivo: desenvolver um código que calcula as raízes (sejam reais ou complexas) de uma equação cúbica
'''


import math

def xR1(q, t, a):
    x1 = -2 * math.sqrt(q) * math.cos(t/3) - (a/3)
    return x1

def xR2(q, t, a):
    x2 = -2 * math.sqrt(q) * math.cos((t + 2 * math.pi) / 3) - (a/3)
    return x2

def xR3(q, t, a):
    x3 = -2 * math.sqrt(q) * math.cos((t - 2 * math.pi) / 3) - (a/3)
    return x3

def xR4(p, s):
    x1 = p + s - (a/3)
    return x1

def xC(p, s):
    x2 = - (1/2)* (p + s) - (a/3)
    return x2

def xCi(p, s):
    x2i = (math.sqrt(3) / 2) * (p - s)
    return x2i
    
print("RESOLUCAO DE EQUACAO CUBICA")

#  entrada de valores:
    
print("insira os 4 coficientes da equacao:")
print("forma da equacao cubica: a*x3 + b*x2 + c*x + d = 0")
a0 = float(input("d = "))  # termo independente
a1 = float(input("c = "))  # x
a2 = float(input("b = "))  # x^2
a3 = float(input("a = "))  # x^3

#  mudanca para a, b e c; tornar o primeiro termo (a3) = 1:

a = a2 / a3
b = a1 / a3
c = a0 / a3

# mudanca para q e r:

q = (a ** 2 - 3 * b) / 9
r = (2 * (a ** 3) - 9 * a * b + 27 * c) / 54

#  determinacao das raizes:

if r ** 2 < q ** 3: # 3 raizes reais
    t = math.acos(r / math.sqrt(q**3))
    x1 = xR1(q, t, a)
    x2 = xR2(q, t, a)
    x3 = xR3(q, t, a)
    print("x1 = {0:.3f} x2 = {1:.3f} x3 = {2:.3f}".format(x1, x2, x3)) 

else:  # 1 raiz real e 2 complexas
    if r > 0:
        sgn = 1

    elif r < 0:
        sgn = -1
        
    p = sgn * (abs(r) + ((r ** 2) - (q ** 3))) ** (1/3)
    
    if p == 0: 
        s = 0
   
    else:
        s = q/p
        
    x1 = xR4(p, s)  # raiz real
    x2 = xC(p, s)  # raiz complexa 1
    xi = xCi(p, s)  # raiz complexa 2

    if xi > 0:
        print("x1 = {0:.3f} x2 = {1:.3f} + {2:.3f}i x3 = {3:.3f} - {4:.3f}i".format(x1, x2, xi, x2, xi))
    
    elif xi < 0:
        print("x1 = {0:.3f} x2 = {1:.3f} {2:.3f}i x3 = {3:.3f} + {4:.3f}i".format(x1, x2, xi, x2, abs(xi)))
