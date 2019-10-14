'''
printar a sequencia de fibonacci

'''

n = int(input("Quantos numeros? ")) 

'''
a partir da posição 3 da sequencia (depois de 0, 1)
o numero será a soma dos dois anteriores
as variáveis n2 e n1 correspondem a esses valores
'''

n2 = 0  
n1 = 1

for x in range (0, n):
    if (x == 0 or x == 1):
        print(x)
    else:
        y = n1 + n2
        print(y)
        n2 = n1
        n1 = y