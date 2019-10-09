# faça um algoritmo para determinar todos os divisores do número N que estão entre os inteiros i1 e i2

print("Este é um programa para achar divisores de um numero em um intervalo")

N = int(input("Escolha um numero para acharmos seus divisores: "))
print("Escolha o intervalo:")
i1 = int(input())
i2 = int(input())

print("Os divisores de {} neste intervalo são: ".format(int(N)))  # .format(N)
for i2 in range (i1, i2):
    if(i2 % N == 0):
        print(i2)



