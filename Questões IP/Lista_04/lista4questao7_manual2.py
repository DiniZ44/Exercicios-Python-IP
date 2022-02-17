LINHAS = 10

'''
vetor = []

i = 0
while i < LINHAS:
    numero = float(input("Digite o %dº número real: " % (i+1)))
    vetor.append(numero)
    i += 1'''

vetor = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

vetor2 = []

i = LINHAS - 1
while i >= 0:
    vetor2.append(vetor[i])
    i -= 1

for i, elemento in enumerate(vetor2):
    print("O elemento do índice %d é %.2f." % (i, elemento))
