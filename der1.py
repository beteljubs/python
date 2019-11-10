# calculo de derivada sem correcao de erro
# uso do quoeficiente de Newton

def f(x):  # funcao escolhida f) = x**2
    f = x**2
    return f

def df_ex(x):  # derivada calculada analiticamente
    f = 2*x
    return f
    
h = 0.001 # quanto menor o valor, mais preciso eh o resultado

x = float(input("x: "))

df = (f(x + h) - f(x))/h  # QUOEFICIENTE DE NEWTON

print("valor exato: {} valor calculado: {}".format(df_ex(x), df))