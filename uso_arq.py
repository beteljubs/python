arq = open("lista1.py","r")  # abrindo o arquivo (deve estar na mesma pasta)

for linha in arq:  # var que representara cada linha de arq (do arquivo lista1)
    valores = linha.split()  # separando valores de cada linha
    print(valores[0])  # printando a primeira palavra de cada linha
    
arq.close()  # fechando o arquivo
