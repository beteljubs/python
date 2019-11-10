# códic calculo de derivada sem correcao de erro
# uso do quoeficiente de Newton

def f(x):
    f = x**2
    return f

def df_ex(x):
    f = 2*x
    return f
    
h = 0.1 # quanto menor o valor, mais preciso eh o resultado

x = float(input())

df = (f(x + h) - f(x))/h

df_ex = df_ex(x)

print("valor exato: {} valor calculado: {}".format(df_ex, df))