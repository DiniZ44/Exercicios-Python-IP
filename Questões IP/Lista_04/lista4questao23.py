ELEMENTOS = 18

LINHAS = 3
COLUNAS = 6

#vetor = []
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
matriz = []

'''i = 0
while i < ELEMENTOS:
    numero = int(input("Digite o %dº número: " % i))
    vetor.append(numero)
    i += 1'''

i = 0
danadinho = 0
while i < LINHAS:
    matriz.append([])
    
    j = 0
    while j < COLUNAS:
        matriz[i].append(vetor[danadinho])
        danadinho += 1
        j += 1
    i += 1


for linha in matriz:
    for coluna in linha:
        print("%d\t" % coluna, end = "")
    
    print("")
