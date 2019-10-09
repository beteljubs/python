# faça um algoritmo para determinar todos os divisores do número N que estão entre os inteiros i1 e i2

print("Este é um programa para achar divisores de um numero em um intervalo")

N = int(input("Escolha um numero para acharmos seus divisores: "))
print("Escolha o intervalo:")
i1 = int(input())
i2 = int(input())

print("Os divisores de {} neste intervalo são: ".format(int(N)))

'''
 uso de for:
 
 for x in range (a, b):
   
 loop de forma que x assume valores de a até b (somando 1 ao x a cada loop)
 
 se escrevermos (a, b, c) obteremos x assumindo valores de a até b aumentando c a cada loop
'''

# print dos valores (no intervalo entre i1 e i2) cujo resto da divisão por N é 0: significando que é um de seus divisores
 
for i2 in range (i1, i2):
    if(i2 % N == 0):
        print(i2)



