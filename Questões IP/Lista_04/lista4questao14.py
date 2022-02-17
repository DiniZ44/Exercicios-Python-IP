matriz = [[70, 55, 71], [17, 1, 48], [150, 15, 27]]

menor = matriz[0][0]
linha_menor = 0

#descobrindo o menor elemento e a linha onde se encontra
for i, linha in enumerate(matriz):
    for coluna in linha:
        if coluna < menor:
            menor = coluna
            linha_menor = i

minmax = matriz[linha_menor][0]
coluna_minmax = 0

for j, coluna in enumerate(matriz[linha_menor]):
    if minmax < coluna:
        minmax = coluna
        coluna_minmax = j
     

print("O minmax é %d." % minmax)
print("A posição é linha = %d / coluna = %d" % (linha_menor, coluna_minmax))

