
def ler_matriz(LINHAS, COLUNAS):
    matriz = []
    i = 0
    while i < LINHAS:
        matriz.append([])
        j = 0
        while j < COLUNAS:
            numero = int(input("Digite o valor para a linha %d e coluna %d: "
                               % (i, j)))
            matriz[i].append(numero)
            j += 1
        i += 1
    
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print("%d\t" % coluna, end=" ")
        print("")

print("Lendo a primeira matriz...")
matriz1 = ler_matriz(2, 2)
print("Lendo a segunda matriz...")
matriz2 = ler_matriz(3, 3)
print("Lendo a terceira matriz...")
matriz3 = ler_matriz(3, 2)

imprimir_matriz(matriz1)
imprimir_matriz(matriz2)
imprimir_matriz(matriz3)
