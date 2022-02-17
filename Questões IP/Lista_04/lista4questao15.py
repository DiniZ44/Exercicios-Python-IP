'''Um elemento A ij de uma matriz é dito ponto de sela da matriz A se, 
e somente se, A ij for, ao mesmo tempo, o menor elemento da linha i e o
maior elemento da coluna j . Faça um programa que carregue uma matriz de
ordem 5 × 7, verifique se a matriz possui ponto de sela e, se possuir,
mostre seu valor e sua localização.'''

mat = [[30, 12, 20], [17, 40, 90], [25, 200, 300]]


for i, linha in enumerate(mat):
    menor = mat[i][0]
    coluna_menor = 0 
    
    #buscando o menor elemento da linha
    for j, coluna in enumerate(mat):
        if mat[i][j] < menor:
            #encontrei algum elemento menor na linha
            menor = mat[i][j]
            coluna_menor = j
    
    #buscando o maior elemento na coluna
    maior = mat[0][coluna_menor]
    linha_maior = 0
    for l, elemento in enumerate(mat):
        if mat[l][coluna_menor] > maior:
            maior = mat[l][coluna_menor]
            linha_maior = l
    
    encontrou = False
    
    if linha_maior == i:
        encontrou = True
        break

if encontrou:
    print("Existe um ponto de sela na matriz.")
    print("O valor do ponto de sela é: %d" % maior)
    print("A localização do ponto de sela é: %dx%d" % (linha_maior,coluna_menor))
else:
    print("Não existe o ponto de sela nessa matriz")
