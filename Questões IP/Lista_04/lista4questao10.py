LINHAS = 2 #dimensão 1
COLUNAS = 2 #dimensão 2

matriz = []

i = 0
while i < LINHAS:
    matriz.append([])
    j = 0
    while j < COLUNAS:
        valor = int(input("Digite um número inteiro (%dx%d): " % (i,j)))
        matriz[i].append(valor)
        
        if i == 0 and j == 0: # se for o primeiro elemento
            maior = valor
        elif valor > maior:
            maior = valor
        
        j += 1
    i += 1

resultante = []
i = 0
while i < LINHAS:
    resultante.append([])
    j = 0
    while j < COLUNAS:
        resultante[i].append(matriz[i][j]*maior)
        j += 1
    i += 1

print(matriz)
print(maior)
print(resultante)
print("")

for linha in resultante:
    for coluna in linha:
        print("%d\t" % coluna, end = "")
    print("")

