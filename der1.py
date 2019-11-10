# calculo de derivada sem correcao de erro
# uso do quoeficiente de Newton

def f(x):  # funcao escolhida f(x) = x**2
    f = x**2
    return f

def df_ex(x):  # derivada calculada analiticamente
    f = 2*x
    return f
    
h = 0.001 # quanto menor o valor, mais preciso eh o resultado

x = float(input("x: "))

# FORMULA DE DIFERENCA ADIANTADA (forward differecnce)
df = (f(x + h) - f(x)) / h  # QUOEFICIENTE DE NEWTON

print("calculo analitico da derivada: f'= {}".format(df_ex(x)))
print("DEFERENCA ADIANTADA:")
print("f' = {}".format(df))

# FORMULA DE DIFERENCA CENTRADA (centered difference)
df = (f(x + h) - f(x - h)) / (2*h) 
 
print("DIFERENCA CENTRADA:")
print("f' = {}".format(df))
