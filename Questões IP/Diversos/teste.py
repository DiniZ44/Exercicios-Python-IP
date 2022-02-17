'''Faça uma função que receba dois números inteiros N e M
e retorna uma matriz NxM preenchida com números inteiros aleatórios.'''


def matriz(n, m):
    import random
    vetor = list(range(0,20)) 

    mat = []
    i = 0
    while i < n:
        mat.append([])
        j = 0
        while j < m:
            random.shuffle(vetor)
            elemento = vetor[0]
            mat[i].append(elemento)
            j+=1
        i+=1
    return print(mat)
    
n = int(input("> "))
m = int(input("> "))
matriz(n, m)